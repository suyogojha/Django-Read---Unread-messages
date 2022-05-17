from email import message
from django.db import models
from django.db.models.fields import BooleanField   
# Create your models here.


SITUATION = (
    ('Read', 'Read'),
    ('Unread', 'Unread'),
)




class Contact(models.Model):
    terms = BooleanField("I agree to the terms and conditions", default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    sub = models.CharField(max_length=100)
    message = models.TextField()
    situation = models.CharField(max_length=100, null=True ,choices=SITUATION, default='Unread')
    
    def __str__(self):
        return self.name
