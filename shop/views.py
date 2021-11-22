import json

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView
from .models import Product, Category, Order, Roasting, Grind, SUBSCRIBE_WEIGHT, \
    SUBSCRIBE_REGULAR, SUBSCRIBE_PERIOD, SUBSCRIBE_DELIVERY_CHOICES, REGION_CHOICES
from .forms import OrderForm, SubscribeForm


class Index(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'coffee'

    def get_queryset(self):
        return Product.objects.filter(popular=True, qty__gt=0)


class CoffeeCatalog(ListView):
    model = Product
    template_name = 'shop/catalog.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CoffeeCatalog, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all().order_by('pk')
        context['category_item'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class OrderView(FormView):
    form_class = OrderForm
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('index')


class ProductView(DetailView):
    model = Product
    template_name = 'shop/product_item.html'


class Subscribe(FormView):
    form_class = SubscribeForm
    template_name = 'shop/subscribe.html'
    success_url = reverse_lazy('subscribe')

    def get_context_data(self, **kwargs):
        context = super(Subscribe, self).get_context_data(**kwargs)
        context['title'] = 'Підписка на каву'
        context['category_item'] = Category.objects.get(pk=1)
        context['product'] = Product.objects.filter(is_subscribe=True).order_by('pk')
        context['roasting'] = Roasting.objects.all()
        context['grind'] = Grind.objects.all()

        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        name = self.request.POST.get('name')
        phone = self.request.POST.get('phone')
        method_delivery = self.request.POST.get('method_delivery')
        region = self.request.POST.get('region')
        city = self.request.POST.get('city')
        address = self.request.POST.get('address')
        product = self.request.POST.get('product')
        grind = self.request.POST.get('grind')
        weight = self.request.POST.get('weight')
        regular = self.request.POST.get('regular')
        period = self.request.POST.get('period')

        roasting = self.request.POST.get('roasting')
        if roasting:
            roasting = Roasting.objects.get(pk=roasting).name

        for i in SUBSCRIBE_DELIVERY_CHOICES:
            if i[0] == method_delivery:
                method_delivery = i[1]
        for i in REGION_CHOICES:
            if i[0] == region:
                region = i[1]
        for i in SUBSCRIBE_WEIGHT:
            if i[0] == weight:
                weight = i[1]
        for i in SUBSCRIBE_REGULAR:
            if i[0] == regular:
                regular = i[1]
        for i in SUBSCRIBE_PERIOD:
            if i[0] == period:
                period = i[1]

        context = {
            'name': name,
            'phone': phone,
            'method_delivery': method_delivery,
            'region': region,
            'city': city,
            'address': address,
            'product': product,
            'roasting': roasting,
            'grind': grind,
            'weight': weight,
            'regular': regular,
            'period': period
        }
        text = f'Ім\'я: {name}, Телефон: {phone}'
        email_html = render_to_string('shop/email2.html', context)
        send_mail('Підписка на каву', text, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET,
                  html_message=email_html)
        instance.save()
        messages.success(self.request, 'Замовлення успішно оформлене. Наш менеджер зв\'яжеться з Вами')
        return super(Subscribe, self).form_valid(form)


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
