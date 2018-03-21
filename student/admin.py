from django.contrib import admin
from .models import Warden, Hostel_name, Hostel_Committee, Mess, Notifications
# Register your models here.
admin.site.register(Hostel_name)
admin.site.register(Hostel_Committee)
admin.site.register(Mess)
admin.site.register(Warden)
admin.site.register(Notifications)