from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('FirstName')
        userlastname = request.POST.get('LastName')
        user_email = request.POST.get('EmailAddress')
        user_password = request.POST.get('Password')
        data = Signup(FirstName=username, LastName=userlastname, EmailAddress=user_email, Password=user_password)
        data.save()
        return HttpResponse("Data saved successfully!")  # You can change this response as needed

    return render(request, 'page/signup.html')
    
