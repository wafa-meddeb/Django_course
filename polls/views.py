from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def home(request):
    backvar = "Hello wafa"
    context = {"fonctionVar" : backvar, "var1": 10,"List1": [10,20,30]}
    return render(request,"index.html" , context) 


