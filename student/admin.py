from django.contrib import admin
from .models import Warden, Hostel_name, Hostel_Committee, Notifications, Allotment_scheme, About_us, Hostel_images
# Register your models here.
admin.site.register(Hostel_name)
admin.site.register(Hostel_Committee)
admin.site.register(Warden)
admin.site.register(Notifications)
admin.site.register(About_us)
admin.site.register(Allotment_scheme)
admin.site.register(Hostel_images)