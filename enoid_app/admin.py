from django.contrib import admin
from .models import TourDate, Message # new

# Register your models here.
admin.site.register(TourDate)
admin.site.register(Message)