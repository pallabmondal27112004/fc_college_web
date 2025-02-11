# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

# @register.filter(name="remove_special")
def replace(value, arg):
    try:
        for i in arg:
            value=value.replace(i, " ")
        value=value.split(",")

        return  value 
    except ValueError:
        return value  

register.filter("remove_special",replace)