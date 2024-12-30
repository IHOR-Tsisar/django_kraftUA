from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Beverage,Cheese, Contact


from django.shortcuts import render


def home(request):
   categories = Category.objects.filter(is_visible=True)
   beverages = Beverage.objects.filter(is_visible=True)
   cheeses = Cheese.objects.filter(is_visible=True)

   context = {
      'categories': categories,
      'beverages': beverages,
      'cheeses': cheeses,
   }
   return render(request, 'product.html', context)








