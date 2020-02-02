from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    return render(request, "index.html")

def usuario1(request):
    return render(request, "usuario1.html")

def handler404(request, exception):
    data = {}
    return render(request, 'myapp/404.html', data)


