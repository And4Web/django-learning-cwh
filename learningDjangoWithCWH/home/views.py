from django.shortcuts import render, HttpResponse

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
  return render(request, 'contact.html')
  # return HttpResponse("Hello, this is Contact page")