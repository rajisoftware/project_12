from django.shortcuts import render

# Create your views here.
def lava(request):
    return render(request,'lava.html')
def kusha(request):
    return render(request,'kusha.html')