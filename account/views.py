from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from account.utils import send_otp_to_user, sign_up_email, sign_in_email
from account.models import *
from django.contrib import messages
from django.http import HttpResponse
from datetime import timedelta

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect("/home/")
  
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        users = User.objects.all()
        for user in users:
            if user.username == username:
                messages.info(request, "Username is already taken")
                return redirect("/")
            if user.email == email:
                messages.info(request, "email is already taken")
                return redirect("/")
            elif password1 != password2:
                messages.info(request, "Password is not match")
                return redirect("/")
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.save()
        messages.info(request, "Account create successfully")
        sign_up_email(email)
        return redirect("/sign_in/")
    return render(request, "account/sign_up.html")

def sign_in(request):
    if request.user.is_authenticated:
        return redirect("/home/")

    if request.method == "POST":
        global email
        email = request.POST.get("email")
        password = request.POST.get("password")

        username = User.objects.get(email = email)

        global user 
        user = authenticate(request, username = username.username, password = password)

        if user is None:
            messages.info(request, "Password or email is wrong")
            return redirect("/sign_in/")
        else:
            request.session['otp']=send_otp_to_user(email)
            request.session.set_expiry(300)
            return redirect("/verify_otp/")
        
    return render(request, "account/sign_in.html")
        
def verify_otp(request):
    if request.user.is_authenticated:
        return redirect("/home/")

    if request.method == "POST":
        otp = request.POST.get("otp")
        otp = int(otp)
        session_otp = request.session.get('otp')

        if session_otp == otp:
            login(request, user)
            sign_in_email(email)
            return redirect("/home/")
        else:
            messages.info(request,"Otp is worng")
            return redirect("/verify_otp/")
        
    return render(request, "account/verify_otp.html")
