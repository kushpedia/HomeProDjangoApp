from django.db import models
from django.contrib.auth.models import User
from services.models import Service
# Create your models here. 
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Service Provider', 'Service Provider'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='static/images/profile_pics/', blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Profiles'
        verbose_name_plural = 'Profiles'

# Service Provider Details model
class ServiceProviderDetails(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='service_provider_details')
    specialization = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    working_hours = models.JSONField()  # Dictionary format for each day: { "monday": "9:00 AM - 6:00 PM", ... }
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Service Provider: {self.user_profile.user.username}"
    class Meta:
        verbose_name = 'ServiceProviderDetails'
        verbose_name_plural = 'Service Provider     Details'
# Customer Booking History model
class BookingHistory(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='booking_history')
    service_name  = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_name')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Pending', 'Pending')])

    def __str__(self):
        return f"Booking - {self.service_name} for {self.user_profile.user.username}"
    class Meta:
        verbose_name = 'BookingHistory'
        verbose_name_plural = 'Booking History'
# Service History model for Service Providers
class ServiceHistory(models.Model):
    service_provider = models.ForeignKey(ServiceProviderDetails, on_delete=models.CASCADE, related_name='service_history')
    service_name = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Pending', 'Pending')])

    def __str__(self):
        return f"Service - {self.service_name} by {self.service_provider.user_profile.user.username}"
    class Meta:
        verbose_name = 'ServiceHistory'
        verbose_name_plural = 'Service History'
# Rating and Review model
class RatingReview(models.Model):
    service_provider = models.ForeignKey(ServiceProviderDetails, on_delete=models.CASCADE, related_name='reviews')
    customer_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    review_text = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.service_provider.user_profile.user.username} by {self.customer_name}"

# Payment Information model
class PaymentInformation(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='payment_info')
    preferred_payment_method = models.CharField(max_length=50)
    card_last_four = models.CharField(max_length=4)

    def __str__(self):
        return f"Payment Info for {self.user_profile.user.username}"
    class Meta:
        verbose_name = 'PaymentInformation'
        verbose_name_plural = 'Payment Information'
# Saved Addresses model
class SavedAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='saved_addresses')
    address_name = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address_name} - {self.user_profile.user.username}"
    class Meta:
        verbose_name = 'SavedAddress'
        verbose_name_plural = 'Saved Address'
# Notification Preferences model
class NotificationPreferences(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='notification_preferences')
    booking_updates = models.BooleanField(default=True)
    promotions = models.BooleanField(default=False)
    review_requests = models.BooleanField(default=True)

    def __str__(self):
        return f"Notifications for {self.user_profile.user.username}"
    class Meta:
        verbose_name = 'NotificationPreferences'
        verbose_name_plural = 'Notification Preferences'
# Account Security model
class AccountSecurity(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='account_security')
    password_last_updated = models.DateField()
    two_factor_auth = models.BooleanField(default=False)

    def __str__(self):
        return f"Security for {self.user_profile.user.username}"

# Payment Card model
class PaymentCard(models.Model):
    payment_info = models.ForeignKey(PaymentInformation, on_delete=models.CASCADE, related_name='saved_cards')
    card_type = models.CharField(max_length=50)
    last_four_digits = models.CharField(max_length=4)
    expiry_date = models.CharField(max_length=7)  # Format: MM/YY

    def __str__(self):
        return f"{self.card_type} ending in {self.last_four_digits} for {self.payment_info.user_profile.user.username}"