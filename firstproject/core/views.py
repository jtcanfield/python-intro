from django.shortcuts import render

# Create your views here.
def greeting(request):
    return HttpResponse("hello worldf")
