from django.shortcuts import render, redirect
from .models import Portfolio
# Create your views here.
def portfolio(request):
    portfolios= Portfolio.objects
    return render(request,'portfolio.html', {'portfolios': portfolios})

def upload(request):
    return render(request,'upload.html')


def create2(request):
    photo = Portfolio()
    photo.title= request.POST['title']
    photo.image = request.FILES['image']
    photo.description = request.POST['description']
    photo.save()
    return redirect('/portfolio')