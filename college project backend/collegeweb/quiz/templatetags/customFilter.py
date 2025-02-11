
from django import template

register = template.Library()


def filterAns(queryset, value):
    try:

        print(queryset)
        return queryset.filter(isCorrect=value)
    except Exception as e:
        print(e)
register.filter("filterAns",filterAns)
# @register.filter
# def catafilter(value,val):
#     return value.filter(catagory_name=val)