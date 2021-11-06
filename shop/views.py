import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
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


class CoffeeCatalog(ListView):
    model = Product
    template_name = 'shop/catalog.html'
    context_object_name = 'coffee'

    def get_queryset(self):
        return Product.objects.filter(category=1)

    def get_context_data(self, **kwargs):
        context = super(CoffeeCatalog, self).get_context_data(**kwargs)
        context['title'] = 'Свежеобжаренный кофе'
        context['subtitle'] = 'Лучшие истории рассказывают за чашечкой кофе'
        return context


class OrderView(FormView):
    form_class = OrderForm
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('index')




def detail(request, slug):
    return HttpResponse(f'{slug} - OK')


def help_form(request):
    context = {
        'name': request.POST['name'],
        'phone': request.POST['phone']
    }
    print(context)
    text = 'Заполнена форма "Нужна помощь"'
    email_html = render_to_string('shop/email.html', context)
    send_mail('Cupman - Заполнена форма "Нужна помощь"', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
              html_message=email_html)
    return JsonResponse({'status': 'OK'})
