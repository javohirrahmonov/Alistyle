from django.shortcuts import render ,redirect
from django.contrib.auth import login, logout , authenticate
from django.views import View
from .models import *
from django.contrib import messages


class RegisterView(View):
    def get(self,request):
        return render(request,"page-user-register.html")

    def post(self,request):
        u = User.objects.create_user(
            username = request.POST.get('e'),
            password = request.POST.get('p'),
        )
        u.email = request.POST.get('e'),
        u.first_name = request.POST.get('fn'),
        u.last_name = request.POST.get('ln'),
        Account.objects.create(
            jins= request.POST.get('g'),
            shahar = request.POST.get('cit'),
            davlat = request.POST.get('c'),
            user = u
        )
        return redirect("login")

class LoginView(View):
    def get(self,request):
        return render(request,"page-user-login.html")

    def post(self,request):
        user = authenticate(
            username=request.POST['l'],
            password=request.POST['p']
        )
        if user is None:
            messages.error(request, 'Login yoki parolda xatolik bor')
            return redirect('login')
        login(request, user)
        return redirect("home")

class Logout_view(View):
        def get(self,request):
            logout(request)
            return redirect("/")