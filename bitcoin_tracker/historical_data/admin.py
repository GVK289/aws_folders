from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.empty_value_display = '(None)'
