from django.shortcuts import redirect, render
from .models import Product

class IDHolder:
    id = 1

def home_page(request):
    response = {}
    product = Product.objects.get(pk=IDHolder.id)
    print(IDHolder.id)
    IDHolder.id += 1
    IDHolder.id %= (Product.objects.count()+1)
    if(IDHolder.id ==0):
        IDHolder.id = 1
    response['product'] = product
    return render(request, 'home.html', response)