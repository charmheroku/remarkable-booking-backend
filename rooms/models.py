from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(
        max_length=100,
        default="",
    )

    country = models.CharField(
        max_length=50,
        default="Slovenia",
    )
    city = models.CharField(
        max_length=80,
        default="Ribchev Laz",
    )

    location = models.CharField(
        max_length=100,
        default="",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    max_total_guests = models.PositiveIntegerField()
    max_total_adults = models.PositiveIntegerField()
    max_total_children = models.PositiveIntegerField()

    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )

    def __str__(self) -> str:
        return self.name


class Amenity(CommonModel):

    """Amenity Definiton"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
