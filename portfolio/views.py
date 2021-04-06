from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    # return HttpResponse("Home main Page")
    return render(request, 'static/portfolio/index.html')