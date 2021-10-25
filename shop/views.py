import json

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from .models import Product, Order
from .forms import OrderForm


class Index(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'coffee'

    def get_queryset(self):
        return Product.objects.filter(popular=True, qty__gt=0)


class OrderView(FormView):
    form_class = OrderForm
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('index')




def detail(request, slug):
    return HttpResponse(f'{slug} - OK')
