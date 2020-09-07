from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    # Subtracts a value from a template variable
    return value - arg