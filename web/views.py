from django.shortcuts import render
from .models import Web_sites
def site(request):
    WB = Web_sites.objects.all()
    return render(request,'web_sites.html',{'WB':WB})
