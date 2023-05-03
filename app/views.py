from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'data':'haI HoW ARe YoU'}
    return render(request,'filter.html',d)