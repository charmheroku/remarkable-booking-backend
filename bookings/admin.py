from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = (
        "user",
        "room",
        "check_in",
        "check_out",
        "guests",
    )
