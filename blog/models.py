#connect with other file
from django.conf import settings
from django.db import models
from django.utils import timezone

#class is defining an object, Post is a model
#model.Model mean Django knows that Post be saved in the database
class Post(models.Model):
    #this is a link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #this is a define text with a limited number of characters
    title =  models.CharField(max_length=200)
    #this is for long text without a limit
    text = models.TextField()
    #this is a date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #this is a function/method and publish is a method
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #__str__ is a method which will give a text with Post title
    def __str__(self):
        return self.title

