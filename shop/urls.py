from django.urls import path
from .views import Index, OrderView, CoffeeCatalog, ProductView, Subscribe, help_form

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('catalog/<slug:slug>', CoffeeCatalog.as_view(), name='coffee_catalog'),
    path('cart/', OrderView.as_view(), name='cart'),
    path('coffee/<slug:slug>', ProductView.as_view(), name='coffee_detail'),
    path('subscribe/', Subscribe.as_view(), name='subscribe'),
    path('help-form/', help_form, name='help_form'),

]
