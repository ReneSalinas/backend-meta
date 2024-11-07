from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.DrinksCategory)
admin.site.register(models.Drinks)
admin.site.register(models.Booking)
admin.site.register(models.Employees)
admin.site.register(models.Menu)