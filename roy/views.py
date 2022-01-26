from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
def samplefunction(request):
    return HttpResponse("hello")
def helloworldfunction (request):
    return render(request,'shajil.html')  
