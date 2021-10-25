from django.urls import path
from .views import Index, OrderView, detail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cart/', OrderView.as_view(), name='cart'),
    path('coffee/<slug:slug>', detail, name='coffee_detail'),
]
