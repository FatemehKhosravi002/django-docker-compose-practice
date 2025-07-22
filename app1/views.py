from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HelloView(request , name):
    res=f"Hello {name} nice to meet you"
    return HttpResponse(res)