from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from datetime import datetime

class Registration(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='media', default='media/34AD2.jpg')

    def get_absolute_url(self):

        return reverse('student:prof', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + '-' + self.department + '-' + str(self.year)

class Notifications(models.Model):
    file = models.FileField()
    message = models.CharField(max_length=500)
    is_new = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(default=datetime.now().date())

    def get_absolute_url(self):
        return reverse('student:notify')

    def __str__(self):
        return self.message
