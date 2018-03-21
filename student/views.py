from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Notifications
from .forms import Loginform
from datetime import datetime



def notify(request):
    all_files = Notifications.objects.all().order_by('-time_stamp')
    for files in all_files:
       day = datetime.now().date() - files.time_stamp.date()
       d = day.days
       if(d <= 2):
           files.is_new = True
       else:
           files.is_new = False
    return render(request, 'student/hostel.html', {'all_files': all_files})

class AddfileView(CreateView):
    model = Notifications
    fields = ['file', 'message']








