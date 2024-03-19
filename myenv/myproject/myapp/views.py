from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def tours(request):
    return render(request,'tours.html')    
def munnar(request):
    return render(request,'munnar.html')
def kovalam(request):
    return render(request,'kovalam.html')    
def tvm(request):
    return render(request,'tvm.html')
def allepy(request):
    return render(request,'allepy.html')    
def vagamon(request):
    return render(request,'vagamon.html')
def varkala(request):
    return render(request,'varkala.html')        
def contact(request):
    return render(request,'contact.html')     