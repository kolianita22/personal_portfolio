from pyexpat.errors import messages
from django.shortcuts import redirect, render
from mysite.forms import ContactForm  
from django.contrib import messages


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save message to database only
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})