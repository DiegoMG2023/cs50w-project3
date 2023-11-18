from django.contrib import admin

# Register your models here.

from .models import (Toppings, menu,user)

admin.site.register(Toppings)


admin.site.register(menu)
admin.site.register(user)