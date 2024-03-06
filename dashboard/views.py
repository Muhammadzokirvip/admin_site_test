from django.shortcuts import render, redirect
from main import models

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)


def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

def create_service(request):
    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        icon = request.POST['icon']
        models.Service.objects.create(
            name = name,
            body = body,
            icon = icon
        )
    return render(request, 'dashboard/service/create.html')

def list_service(request):
    service = models.Service.objects.all()
    context = {
        'servie':service
    }
    return render(request, 'dashboard/service/list.html', context)


def create_aboutus(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body,
        )
    return render(request, 'dashboard/aboutus/create.html')


def list_aboutus(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/list.html', context)


def create_price(request):
    if request.method == 'POST':
        title = request.POST['name']
        body = request.POST['body']
        price = request.POST['icon']
        models.Price.objects.create(
            title = title,
            body = body,
            price = price
        )
    return render(request, 'dashboard/price/create.html')

def list_price(request):
    price = models.Price.objects.all()
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/list.html', context)