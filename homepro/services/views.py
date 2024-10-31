from django.shortcuts import render
from .models import Service, ServiceCategory  # Adjust according to your app's models

def services_page(request):
    services = Service.objects.all() 
    categories= ServiceCategory.objects.all()
    # Fetch all services
    return render(request, 'services_page.html', {'services': services, 'categories':categories})