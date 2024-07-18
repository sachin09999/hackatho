from django.contrib import admin
from .models import Restaurant, RegularPizza, SicilianPizza, Toppings, Sub, Pasta, Salad, DinnerPlatters, UserOrder, SavedCarts
from tinymce.widgets import TinyMCE
from django.db import models

class RestaurantAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class RegularPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class SicilianPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(RegularPizza, RegularPizzaAdmin)
admin.site.register(SicilianPizza, SicilianPizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatters)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
