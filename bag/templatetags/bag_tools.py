from django import template

register = template.Library()

# Check out creating custom template tags and filters in the Django docs
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
