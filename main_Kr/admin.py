from django.contrib import admin

from django.contrib import admin
from .models import Beverage, Cheese, Contact, AboutUs,Category

admin.site.register(Beverage)
admin.site.register(Cheese)
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(Category)