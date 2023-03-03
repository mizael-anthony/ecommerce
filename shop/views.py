from django.core import paginator
from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item_name')

    #search code
    if item_name != '' and item_name is not None:
        product_objects = Product.objects.filter(title__icontains=item_name)

    #paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)


    
    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_object = Product.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product_object': product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        adress = request.POST.get('adress', '')
        contact = request.POST.get('contact', '')


        order = Order(items=items, name=name, email=email, adress=adress, contact=contact)
        order.save()




    return render(request, 'shop/checkout.html')