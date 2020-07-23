from django.db import models
from django.utils.html import format_html


# Create your models here.
class PriceHistory(models.Model):
    
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    volume = models.IntegerField()
    total_btc = models.IntegerField(default=0)

from django.contrib import admin

# class Customer(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     created_on = models.DateField(auto_now=True)
#     color_code = models.CharField(max_length=6)

#     def colored_name(self):
#         return format_html(
#             '<span style="color: #{};">{} {}</span>',
#             self.color_code,
#             self.first_name,
#             self.last_name,
#         )

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    birthday = models.DateField()

    def born_in_fifties(self):
        return self.birthday.strftime('%Y')[:3] == '195'
    born_in_fifties.boolean = True

class PersonAdmin(admin.ModelAdmin):
    # list_display = ('__str__', 'first_name')
    list_display = ('first_name', 'born_in_fifties')

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name')

# def upper_case_name(obj):
#     return ("%s %s" % (obj.first_name, obj.last_name)).upper()
# upper_case_name.short_description = 'Name'

# class PersonAdmin(admin.ModelAdmin):
#     list_display = (upper_case_name,)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'author_first_name')

    def author_first_name(self, obj):
        return obj.author.first_name

    author_first_name.admin_order_field = 'author__first_name'

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(id__in=[1,2])
        return qs.filter(author=request.user)
