from django.contrib import admin
from .models import students,cources,testimonial
# Register your models here.
class studentsAdmin(admin.ModelAdmin):
    list_display=("image","name","job")

admin.site.register(students)
admin.site.register(cources)
admin.site.register(testimonial)