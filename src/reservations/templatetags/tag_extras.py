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

@register.filter
def totalResDay(day):
    timeslots = day.timeslot_set.all()
    count = 0

    for timeslot in timeslots:
        n = timeslot.getCurrentCapacity()
        count += n
    
    return count