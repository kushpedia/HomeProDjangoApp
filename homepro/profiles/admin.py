from django.contrib import admin
from .models import (
    UserProfile,
    ServiceProviderDetails,
    BookingHistory,
    ServiceHistory,
    RatingReview,
    PaymentInformation,
    SavedAddress,
    NotificationPreferences,
    AccountSecurity,
    PaymentCard)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ServiceProviderDetails)
admin.site.register(BookingHistory)
admin.site.register(ServiceHistory)
admin.site.register(RatingReview)
admin.site.register(PaymentInformation)
admin.site.register(SavedAddress)
admin.site.register(NotificationPreferences)
admin.site.register(AccountSecurity)
admin.site.register(PaymentCard)