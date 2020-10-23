from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Meta:
    managed = True


class Squirrels(models.Model):
    X = models.FloatField(
        help_text=_('Longitude'),
    )
    Y = models.FloatField(
        help_text=_('Latitude'),
    )
    Unique_squirrel_id = models.CharField(
        max_length=100,
        primary_key=True,
        default=None,
    )
    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = (
        (PM, 'PM'),
        (AM, 'AM'),
    )
    Shift = models.CharField(
        max_length=100,
        choices=SHIFT_CHOICES,
        blank=True,
    )
    Date = models.DateField(
        blank=True,
    )
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    AGE_CHOICES = (
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
    )
    Age = models.CharField(
        max_length=100,
        choices=AGE_CHOICES,
        blank=True,
        null=True,)
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )

    Primary_Fur_Color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        null=True,
        blank=True,
    )
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )

    Location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        null=True,
        blank=True,
    )
    Specific_location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    TRUE = 'TRUE'
    FALSE = 'FALSE'
    CHOICES = (
        (TRUE, 'TRUE'),
        (FALSE, 'FALSE'),
    )
    Running = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Chasing = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Climbing = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Eating = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Foraging = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Other_activities = models.CharField(
        max_length=100,
        null=True,
        blank=True,)
    Kuks = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)

    Quaas = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Moans = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Tail_flags = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Tail_twitches = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Approaches = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Indifferent = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)
    Runs_from = models.CharField(
        max_length=100,
        choices=CHOICES,
        blank=True,)

    def __str__(self):
        return self.Unique_squirrel_id

    def get_absolute_url(self):
        return reverse('squirrels-detail', kwargs={'id': self.Unique_squirrel_id})
# Create your models here.
