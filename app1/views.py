from django.shortcuts import render,redirect
from .models import Contact


def home_view(request):
    return render(request,'index.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(name, email, message)

        if email:
            email = email.strip().lower()

            # Check if a contact with this email already exists
            contact, created = Contact.objects.get_or_create(email=email, defaults={'name': name, 'message': message})
            
            if not created:
                # If it exists, update the message (and optionally the name)
                contact.message = message
                contact.name = name  # optional, if you want to update name too
                contact.save()

        return redirect('contact')

    return render(request, 'index.html')



# Create your views here.
