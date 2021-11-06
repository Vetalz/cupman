from django.urls import path
from .views import Index, OrderView, CoffeeCatalog, detail, help_form

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('catalog/', CoffeeCatalog.as_view(), name='coffee_catalog'),
    path('cart/', OrderView.as_view(), name='cart'),
    path('coffee/<slug:slug>', detail, name='coffee_detail'),
    path('help-form/', help_form, name='help_form')
]
