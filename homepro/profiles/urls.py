from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.user_login,name='user_login'),
    path('profile/',views.profile_view,name='profile'),
    
    path('logout/',views.logout_user,name='logout_user'),
    path('',views.home,name='home'),
    path('password-reset/', views.password_reset, name='password_reset'),
    
]