from django.db import models

# Create your models here.

"""
Models to define:

- message
    - card (horizontal view?)
    - letter (vertical view)
- 

questions:
* should we also allow vertical for cards?
* upload image -> upload 1 or multiple?


other:
* maybe for now use local storage

"""

class Message(models.Model):
    # super class to Card & Letter

    date_recieved = models.DateField()
    date_opened = models.DateField()

    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100) # may not be neccesary

    content = models.TextField()

    orientation = None

    class Meta:
        abstract = True

class Card(Message):

    image = models.ImageField() 


    pass

class Letter(Message):


    pass

