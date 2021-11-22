from django.forms import ModelForm, RadioSelect, HiddenInput, TextInput, Select, NumberInput
from .models import Order, Subscribe, Product


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['method_delivery', 'name', 'phone', 'region', 'city', 'new_post_office',
                  'address', 'comment', 'method_payment', 'product']
        widgets = {
            'name': TextInput(attrs={"class": "form-control", "id": "input-name", "aria-describedby": "nameHelp",
                                   "placeholder": "ФИО"}),
            'phone': TextInput(attrs={"class": "form-control", "id": "phone", "aria-describedby": "nameHelp",
                                     "placeholder": "Телефон"}),
            'region': Select(attrs={"class": "form-control form-select", "id": "input-region",
                                    "aria-describedby": "nameHelp"}),
            'city': TextInput(attrs={"class": "form-control", "id": "input-city", "aria-describedby": "nameHelp",
                                      "placeholder": "Город"}),
            'new_post_office': NumberInput(attrs={"class": "form-control", "id": "input-new_post",
                                                  "aria-describedby": "nameHelp",
                                                  "placeholder": "№ отделения Новой Почты"}),
            'address': TextInput(attrs={"class": "form-control", "id": "input-address", "aria-describedby": "nameHelp",
                                      "placeholder": "Домашний адрес для курьерской доставки"}),
            'comment': TextInput(attrs={"class": "form-control", "id": "input-comment", "aria-describedby": "nameHelp",
                                      "placeholder": "Комментарий по желанию"}),
            'product': TextInput(attrs={"class": "hidden", "id": "input-product"})
        }


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['product', 'roasting', 'grind', 'name', 'phone', 'method_delivery', 'region', 'city', 'address',
                  'weight', 'regular', 'period']

        widgets = {
            'name': TextInput(attrs={"class": "form-control", "id": "input-name-2", "aria-describedby": "nameHelp",
                                     "placeholder": "ПІБ"}),
            'phone': TextInput(attrs={"class": "form-control", "id": "phone", "aria-describedby": "nameHelp"}),
            'region': Select(attrs={"class": "form-select", "id": "input-region-2",
                                    "aria-describedby": "nameHelp"}),
            'city': TextInput(attrs={"class": "form-control", "id": "input-city-2", "aria-describedby": "nameHelp",
                                     "placeholder": "Місто"}),
            'address': TextInput(attrs={"class": "form-control", "id": "input-address-2", "aria-describedby": "nameHelp",
                                        "placeholder": "Домашня адреса або № відділення Нової Пошти"}),
            'product': TextInput(attrs={"class": "hidden", "id": "input-product"}),
            'roasting': TextInput(attrs={"class": "hidden", "id": "input-roasting"}),
            'grind': TextInput(attrs={"class": "hidden", "id": "input-grind"}),
        }
