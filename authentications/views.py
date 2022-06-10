from django.shortcuts import render
from django.views.generic.edit import CreateView
from authentications.models import Users
from authentications.forms import RegisterUser,LoginUSer
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
# Create your views here.
class UserRegistraion(CreateView):
    template_name = 'authentications/register.html'
    form_class = RegisterUser
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        clean_data = form.cleaned_data
        user = authenticate(username=clean_data['username'],
                            password=clean_data['password1'])
        login(self.request, user)
        return result

class UserLogin(CreateView):
    template_name = 'authentications/login.html'
    form_class = LoginUSer
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        clean_data = form.cleaned_data
        user = authenticate(username=clean_data['username'],
                            password=clean_data['password1'])
        login(self.request, user)
        return result
