from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Cleaning_Product
from . forms import HistoryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all() # Retrieve all shoes
    return render(request, 'shoes/index.html', {
        'shoes': shoes
    })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    id_list = shoe.cleaning_products.all().values_list('id')
    cleaning_products_shoe_doesnt_have = Cleaning_Product.objects.exclude(id__in=id_list)
    history_form = HistoryForm()
    return render(request, 'shoes/detail.html', {
        'shoe': shoe , 'history_form': history_form,
        'cleaning_products': cleaning_products_shoe_doesnt_have
    })

def assoc_cleaning_product(request, shoe_id, cleaning_product_id):
    Shoe.objects.get(id=shoe_id).cleaning_products.add(cleaning_product_id)
    return redirect('detail', shoe_id=shoe_id)

def unassoc_cleaning_product(request, shoe_id, cleaning_product_id):
    Shoe.objects.get(id=shoe_id).cleaning_products.remove(cleaning_product_id)
    return redirect('detail', shoe_id=shoe_id)

class ShoeCreate(CreateView):
    model = Shoe
    fields = ['name', 'maker', 'color', 'release_year', 'price']

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['maker', 'color', 'release_year', 'price']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes'

def add_history(request, shoe_id):
    form = HistoryForm(request.POST)
    if form.is_valid():
        new_history = form.save(commit=False)
        new_history.shoe_id = shoe_id
        new_history.save()
    return redirect('detail', shoe_id=shoe_id)

class Cleaning_ProductList(ListView):
    model = Cleaning_Product

class Cleaning_ProductDetail(DetailView):
    model = Cleaning_Product

class Cleaning_ProductCreate(CreateView):
    model = Cleaning_Product
    fields = '__all__'

class Cleaning_ProductUpdate(UpdateView):
    model = Cleaning_Product
    fields = ['name', 'description' 'price']

class Cleaning_ProductDelete(DeleteView):
    model = Cleaning_Product
    success_url = '/cleaning_products'

