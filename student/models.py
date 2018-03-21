from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Hostel_name(models.Model):
    name = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('individualhostel:notifications', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Mess(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE)
    mess_number = models.IntegerField()
    mess_maharaja = models.CharField(max_length=300)

    def __str__(self):
        return 'Mess no. - ' + str(self.mess_number) + ' of ' + self.hostel.name

class Warden(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE)
    warden_name = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=10)
    profile_photo = models.ImageField(upload_to='media', default='media/default_dp.png')

class Hostel_Committee(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='media', default='media/default_dp.png')

class Notifications(models.Model):
    file = models.FileField()
    message = models.CharField(max_length=1000)
    is_new = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse('student:notify')

    def __str__(self):
        return self.message
