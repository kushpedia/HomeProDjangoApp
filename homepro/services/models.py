from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    categoryImage = models.ImageField(upload_to='static/images/category_images/', blank=True, null=True)  # category images
    
    # parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'ServiceCategory'
        verbose_name_plural='Categories'
        
    @property
    def imageURL(self):
        try:
            url = self.categoryImage.url
        except:
            url = ''
        return url

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
    
class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Assuming User model is from Django's auth or custom User
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    specialization = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    availability = models.BooleanField(default=True)
    topServiceProvider = models.BooleanField(default=True)
    


    def __str__(self):
        return self.name
        
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name    
    
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"{self.customer.name} - {self.service.name}"
    
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.name} for {self.service_provider.name}"