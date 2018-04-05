from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Hostel_name(models.Model):
    name = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('student:notifications', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Warden(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE)
    warden_name = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=10)
    profile_photo = models.ImageField(upload_to='media', default='default_dp.png')
    warden_position = models.CharField(max_length=100, null=True)
    warden_email_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.warden_name + ' - warden of ' + self.hostel.name

class Hostel_Committee(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=300)
    member_post = models.CharField(max_length=100, null=True)
    member_email_id = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='media', default='default_dp.png')

    def __str__(self):
        return self.member_name + ' - hec of ' + self.hostel.name

class Notifications(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    message = models.CharField(max_length=1000)
    is_new = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse('student:notify')

    def __str__(self):
        return self.message

class About_us(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE, null=True)
    para_1 = models.CharField(max_length=1000)
    para_2 = models.CharField(max_length=2000)

    def __str__(self):
        return self.hostel.name + " - About us"

class Allotment_scheme(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE, null=True)
    scheme = models.CharField(max_length=1000)

    def __str__(self):
        return self.hostel.name + " - Scheme"

class Hostel_images(models.Model):
    hostel = models.ForeignKey(Hostel_name, on_delete=models.CASCADE, null=True)
    image_1 = models.ImageField(upload_to='media', default='default_dp.png')
    image_2 = models.ImageField(upload_to='media', default='default_dp.png')
    image_3 = models.ImageField(upload_to='media', default='default_dp.png')

    def __str__(self):
        return self.hostel.name + " - images"
