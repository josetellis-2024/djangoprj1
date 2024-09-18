from  django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')