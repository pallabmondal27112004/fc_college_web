from django.contrib import admin
from .models import catagory,question,answer
# Register your models here.
admin.site.register(catagory)



class answeradmin(admin.StackedInline):
    model=answer

class questionadmin(admin.ModelAdmin):
    inlines=[answeradmin]
admin.site.register(question,questionadmin)
admin.site.register(answer)
