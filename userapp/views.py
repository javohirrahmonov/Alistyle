from django.shortcuts import render ,redirect
from django.contrib.auth import login, logout , authenticate
from django.views import View
from .models import *


class RegisterView(View):
    def get(self,request):
        return render(request,"page-user-register.html")

class LoginView(View):
    def get(self,request):
        return render(request,"page-user-login.html")