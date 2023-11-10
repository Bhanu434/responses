from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def abd(request):
    return render(request,'abd.html') 
def virat(request):
    return HttpResponse ('<h1>Great player</h1>')