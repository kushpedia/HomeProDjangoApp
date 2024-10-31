from django.contrib import admin
from .models import Ticket, TicketCategory, TicketComment

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'created_by', 'assigned_to', 'created_at']
    search_fields = ['title', 'created_by__username']
    list_filter = ['status', 'priority', 'created_at']

@admin.register(TicketCategory)
class TicketCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'created_by', 'created_at']
    search_fields = ['ticket__title', 'created_by__username']