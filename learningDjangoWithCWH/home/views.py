from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
  context = {
    "variable1": "Python",
    "variable2": "JavaScript"
  }
  return render(request, "index.html", context)
  # return HttpResponse("Hello, this is my first django project")

def about(request):
    return render(request, 'about.html')
  # return HttpResponse("Hello, this is About page")

def services(request):
  return render(request, 'services.html')
  # return HttpResponse("Hello, this is Services page")

def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email') 
    phone = request.POST.get('phone')     
    desc = request.POST.get('desc') 
    contact = Contact(name=name, email=email, phone=phone, desc=desc, created_at=datetime.today())
    contact.save()
  return render(request, 'contact.html')
  #return HttpResponse("Hello, this is Contact page")