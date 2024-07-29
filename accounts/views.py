from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SaleForm
from .forms import ProductForm
from .forms import ExistingProductForm
import pandas as pd
from django.db.models import Sum
from .filters import ProductFilter
from django.shortcuts import get_object_or_404, redirect

from accounts.models import *

# Create your views here.
def home(response):
    products_count = Product.objects.aggregate(products_count=Sum("quantity"))["products_count"]
    no_stock = Product.objects.filter(quantity=0)
    no_stock_count = no_stock.count()
    sales = Sale.objects.filter(sale_date__date=timezone.now().date())
    sales_count = sales.aggregate(sales_count = Sum("quantity_sold"))["sales_count"]
    context = {"products_count":products_count,"sales_count":sales_count, "no_stock_count":no_stock_count}
    return render(response, 'accounts/dashboard.html',context)



def products(response):
    products = Product.objects.all()
    myFilter = ProductFilter(response.GET, queryset=products)
    products = myFilter.qs
    context = {"products":products,"myFilter":myFilter}
    return render(response, 'accounts/products.html',context)



def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            product = sale.product
            if product.quantity >= sale.quantity_sold:
                product.quantity -= sale.quantity_sold
                product.save()
                sale.selling_price = product.selling_price
                sale.save()
                return redirect('/')
            else:
                return render(request,'accounts/no_stock.html')
    else:
        form = SaleForm()
    return render(request, 'accounts/create_sale.html', {'form': form})


def sales_list(request):
    sales = Sale.objects.filter(sale_date__date=timezone.now().date())
    return render(request, 'accounts/sales_list.html', {'sales': sales})

def export_sales_to_excel(request):
    sales = Sale.objects.filter(sale_date__date=timezone.now().date())
    data = [{
        'Product': sale.product.name,
        'Quantity Sold': sale.quantity_sold,
        'Selling Price': sale.selling_price,
        'Profit': sale.profit,
        'Sale Date': sale.sale_date.replace(tzinfo=None)
    } for sale in sales]
    

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    today_date = timezone.now().date()
    name_file = f"sales_report_{today_date}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{name_file}"'
    df.to_excel(response, index=False)
    return response

def no_stock_show(response):
    no_stocks = Product.objects.filter(quantity=0)
    return render(response,'accounts/no_stock_show.html',{"no_stocks":no_stocks})


def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request,'accounts/create_product.html', context)

def delete_product(request, pk): 
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', {'product': product})


def add_existing_product(request):
    form = ExistingProductForm()
    if request.method == 'POST':
        form = ExistingProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            product.quantity += quantity
            product.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/add_existing_product.html', context)