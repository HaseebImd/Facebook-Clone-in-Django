from django.http import HttpResponse
from django.shortcuts import render



def home_view(request):
    
    hello="Hello"
    context={
        
        'hello':hello,

    }
    return render(request,'main/home.html',context)