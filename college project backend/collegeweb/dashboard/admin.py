from django.contrib import admin
from .models import assignment,assignmentlist
from .models import menterList
# Register your models here.
admin.site.register(assignmentlist)
admin.site.register(assignment)
admin.site.register(menterList)