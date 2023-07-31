from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
    """
    Represents a form for creating a new message.
    """
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
