from django.db import models
from django.templatetags.static import static # new

# Create your models here.
# Create model to represent tour dates for the band
class TourDate(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    tickets_remaining = models.IntegerField(default=0)
    image_url = models.URLField(default=static('images/default-image.jpg'))

    def __str__(self):
        return f'''{self.date}
                   {self.location}
                   {self.venue}
        ''' 

# Create a model for the messages or inquiries from the "Contact Page"
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'''{self.name}
                   {self.email}
                   {self.message}
        '''