from django.shortcuts import render
from . models import Product

# Create your views here.
def index(req):
    products = Product.objects.all()
    context ={}
    context['products'] = products
    return render(req,"index.html",context)

def prodDetails(req,pid):
    products = Product.objects.get(product_id = pid)
    context ={}
    context['products'] = products
    return render(req,"productDetail.html",context)

def viewCart(req):
    return render(req,"cart.html")

from django.db.models import Q
def search(req):
    query = req.POST['q']
    print(f"Query is {query}")
    if not query:
        result = Product.objects.all()
    else:
        result = Product.objects.filter(
            Q(product_name__icontains = query)|
            Q(desc__icontains = query)|
            Q(price__icontains = query)
            
        )
    return render(req,"search.html",{'results':result,'query':query})