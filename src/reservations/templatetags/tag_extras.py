from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    # Subtracts a value from a template variable
    return value - arg


@register.filter
def userResExists(timeslot, customer):
    res_exists = timeslot.reservation_set.filter(customer=customer).exists()
    return res_exists