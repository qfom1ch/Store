from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .models import User
from django.contrib import auth
from django.urls import reverse


# class Login(CreateView):
#     model = User
#     form_class = UserLoginForm
#     template_name = 'users/login.html'
#     success_url = '/login'
#     context_object_name = 'formlogin'


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password ) # проверяет, есть ли пользователь такой.
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/registration.html', context)



def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title':'Store - Профиль',
        'form':form
               }
    return render(request, 'users/profile.html',context)