from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def ABM_Stock(request):
    return render(request,'ABM_Stock.html')