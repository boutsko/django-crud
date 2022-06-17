from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views.generic.edit import UpdateView
from .models import CRUD
from .forms import CRUDFORM
from django.views.generic import ListView, CreateView, DeleteView, DetailView

# home view
class Home(ListView):
    model = CRUD
    template_name = 'app/base.html'
 
# create view
class Create(CreateView):
    model = CRUD
    template_name = 'app/create.html'
    form_class = CRUDFORM

    # if the form, submits, to go back to the homepage automatically
    def get_success_url(self):
        return reverse('main:home')

# detail view
class Detail(DetailView):
    model = CRUD
    template_name = 'app/detail.html'

# update view
class Update(UpdateView):
    model = CRUD
    template_name = 'app/create.html'
    form_class = CRUDFORM

    # if the form, submits, to go back to the homepage automatically
    def get_success_url(self):
        return reverse('main:home')

# delete view
class Delete(DeleteView):
    model = CRUD
    template_name = 'app/delete.html'
    # if the form, submits, to go back to the homepage automatically
    def get_success_url(self):
        return reverse('main:home')


# Create your views here.
