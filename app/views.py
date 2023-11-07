from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader
# Create your views here.
def product(request):
    b1=Product.objects.all().values()
    return render(request, 'product.html', {'b1': b1})
    

