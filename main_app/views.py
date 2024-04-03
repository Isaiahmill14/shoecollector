from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe
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
    history_form = HistoryForm()
    return render(request, 'shoes/detail.html', {
        'shoe': shoe , 'history_form': history_form
    })

def add_history(request, shoe_id):
    form = HistoryForm(request.POST)
    if form.is_valid():
        new_history = form.save(commit=False)
        new_history.shoe_id = shoe_id
        new_history.save()
    return redirect('detail', shoe_id=shoe_id)

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['maker', 'color', 'release_year', 'price']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes'