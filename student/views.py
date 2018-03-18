from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Registration, Notifications
from .forms import Loginform
from datetime import datetime


class reg(CreateView):
    model = Registration
    fields = ['name', 'hostel_name', 'department', 'year', 'mess_number', 'profile_image']

class DetailView(generic.DetailView):
    model = Registration
    template_name = 'student/profile.html'

class LoginFormView(View):
    form_class = Loginform
    template_name = 'student/login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('student:reg')

        return render(request, self.template_name, {'form': form})

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








