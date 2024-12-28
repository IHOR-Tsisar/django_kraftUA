from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Beverage,Cheese, Contact


from django.shortcuts import render

def home(request):
   categories = Category.objects.filter(is_visible=True)
   beverages = Beverage.objects.all()
   cheeses = Cheese.objects.all()
   contacts = Contact.objects.all()

   return f'{categories}\n{beverages}\n{cheeses}\n{contacts}'




