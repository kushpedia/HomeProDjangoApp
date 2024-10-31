from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.services_page, name='services_page'),
]
