from django.db import models

from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort','name')

    def __str__(self):
        return self.name


class Beverage(models.Model):
    name = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=6, decimal_places=2, help_text="Об'єм у мл")
    alcohol_content = models.DecimalField(max_digits=4, decimal_places=2, help_text="Вміст алкоголю у %")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/beverages/')
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='beverages')
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort','name')

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Вага у грамах")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/cheeses/')
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cheeses')
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort','name')

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/about_us/')
    is_visible = models.BooleanField(default=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} ({self.email}) on {self.created_at}"

# class OrderItem(models.Model):







