from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Deskripsi,Barang

# Create your views here.
def index(request):
    barangs = Barang.objects.all()
    return render(request, 'polls/index.html',{'barangs':barangs})

