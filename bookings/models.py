from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    """Booking Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for: {self.user}"
