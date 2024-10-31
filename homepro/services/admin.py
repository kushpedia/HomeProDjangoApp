from django.contrib import admin
from .models import ServiceCategory,Service,ServiceProvider,Customer,Booking,Review
# Register your models here.
admin.site.register(ServiceCategory)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Review)
