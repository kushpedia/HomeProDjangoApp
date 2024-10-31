from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import (
    UserProfile,
    
)
from .forms import ProfilePictureForm


# Create your views here.
# @login_required(login_url='user_login')
def home(request):
    
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid Login credentials'})    
    
    return render(request, 'login.html')
def password_reset(request):
    return render(request, 'passwordReset.html')
# log out user
@login_required(login_url='user_login')
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    # Redirect to the login page
    return redirect(reverse('user_login'))

# Profile view

@login_required(login_url='user_login')
def profile_view(request):   
    
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        # Handle profile picture upload
        picture_form = ProfilePictureForm(request.POST, request.FILES, instance=user_profile)
        if picture_form.is_valid():
            picture_form.save()
            return redirect('profile')  # Refresh page after updating picture
    else:
        picture_form = ProfilePictureForm(instance=user_profile)
        
        
        
    service_provider_details = getattr(user_profile, 'service_provider_details', None)
    booking_history = user_profile.booking_history.all()
    saved_addresses = user_profile.saved_addresses.all()
    payment_info = getattr(user_profile, 'payment_info', None)
    notification_preferences = getattr(user_profile, 'notification_preferences', None)
    account_security = getattr(user_profile, 'account_security', None)
    
    context = {
        'picture_form': picture_form,
        "user_profile": user_profile,
        "service_provider_details": service_provider_details,
        "booking_history": booking_history,
        "saved_addresses": saved_addresses,
        "payment_info": payment_info,
        "notification_preferences": notification_preferences,
        "account_security": account_security,
    }
    return render(request, "profile.html", context)

