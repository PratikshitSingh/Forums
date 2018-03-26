from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Notifications, Mess, Warden, Hostel_Committee, Hostel_name, About_us, Allotment_scheme, Hostel_images
from .forms import Loginform
from datetime import datetime


def notify(request, pk):
    all_notifications = Notifications.objects.filter(hostel=pk).order_by('-time_stamp')
    all_mess = Mess.objects.filter(hostel=pk)
    all_wardens = Warden.objects.filter(hostel=pk)
    all_hec = Hostel_Committee.objects.filter(hostel=pk)
    all_hostels = Hostel_name.objects.filter(id=pk)
    all_images = Hostel_images.objects.filter(id=pk)
    all_about = About_us.objects.filter(id=pk)
    all_scheme = Allotment_scheme.objects.filter(id=pk)
    for files in all_notifications:
       day = datetime.now().date() - files.time_stamp.date()
       d = day.days
       if(d <= 2):
           files.is_new = True
       else:
           files.is_new = False
    return render(request, 'student/hostel.html',
                  {'all_notitfications': all_notifications,
                   'all_mess': all_mess,
                   'all_hec': all_hec,
                   'all_wardens': all_wardens,
                   'all_hostels': all_hostels,
                   'all_images': all_images,
                   'all_about': all_about,
                   'all_scheme': all_scheme
                   })

class AddfileView(CreateView):
    model = Notifications
    fields = ['file', 'message']








