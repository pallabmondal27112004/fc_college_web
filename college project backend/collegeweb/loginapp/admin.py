from django.contrib import admin

# Register your models here.
from .models import customeruser, catagory
admin.site.register(catagory)
admin.site.register(customeruser)