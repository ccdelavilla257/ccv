from django.contrib import admin
from .models import ContactMessage
from django.utils.html import format_html


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "sent_at", "is_read", "message_preview"]
    list_filter = ["is_read", "sent_at"]
    list_editable = ["is_read"]
    search_fields = ["name", "email", "subject", "message"]
    readonly_fields = ["name", "email", "phone", "subject", "message", "sent_at"]
    date_hierarchy = "sent_at"

    def message_preview(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    message_preview.short_description = "Vista previa"

    fieldsets = (
        ("Datos del contacto", {"fields": ("name", "email", "phone")}),
        ("Mensaje", {"fields": ("subject", "message")}),
        ("Estado", {"fields": ("is_read", "sent_at")}),
    )

    def has_add_permission(self, request):
        return False  # No permitir crear mensajes manualmente
