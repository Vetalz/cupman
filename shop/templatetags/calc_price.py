from django import template

register = template.Library()


@register.simple_tag
def calc_price(price, percent):
    new_price = round(price - price / 100 * percent)
    return new_price
