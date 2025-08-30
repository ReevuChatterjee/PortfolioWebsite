from django.shortcuts import render,redirect
from .models import Contact


def home_view(request):
    return render(request,'index.html')

def submit_contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        print(name,email,message)

    if email:
        email=email.strip().lower()
    
    contact=Contact(
        name=name,
        email=email,
        message=message
    )

    contact.save()

    return render(request,'index.html')


# Create your views here.
