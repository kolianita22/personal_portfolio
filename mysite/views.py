from django.shortcuts import render
from mysite.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_entry = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        contact_entry.save()
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')