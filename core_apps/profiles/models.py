from autoslug import AutoSlugField

from cloudinary.models import CloudinaryField

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedModel


User = get_user_model()


def get_user_username(instance: "Profile") -> str:
    return instance.user.username



class Profile(TimeStampedModel):
    class GenderChoices(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")
        # No other gender options, because we are not accepting transgender users!!!!!

    class OccupationChoices(models.TextChoices):
        Mason = "mason", _("Mason")
        Carpenter = "carpenter", _("Carpenter")
        Plumber = "plumber", _("Plumber")
        Roofer = "roofer", _("Roof")
        Painter = "painter", _("Painter")
        Electrician = "electrician", _("Electrician")
        HVAC = "hvac", _("HVAC")
        Tenant = "tenant", _("Tenant")


    user = models.OneToOneField( # We can access the profile with user.profile
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    avatar = CloudinaryField(
        verbose_name=_("Avatar"),
        blank=True,
        null=True,
    )

    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=10,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE
    )

    bio = models.TextField(
        verbose_name=_("Biography"),
        blank=True,
        null=True,
    )

    occupation = models.CharField(
        verbose_name=_("Occupation"),
        max_length=20,
        choices=OccupationChoices.choices,
        default=OccupationChoices.Tenant
    )

    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        max_length=30,
        default="+359888456789"
    )

    country_of_origin = CountryField(
        verbose_name=_("Country"),
        default="BG"
    )

    city_of_origin = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Sofia"
    )

    report_count = models.IntegerField(
        verbose_name=_("Report Count"),
        default=0
    )

    reputation = models.IntegerField(
        verbose_name=_("Reputation"),
        default=100
    )

    slug = AutoSlugField(
        populate_from=get_user_username,
        unique=True,
    )


    @property
    def is_banned(self) -> bool:
        return self.report_count >= 5


    def update_reputation(self) -> None:
        self.reputation = max(0, 100 - self.report_count * 20)

    def save(self, *args, **kwargs) -> None:
        self.update_reputation()
        super().save(*args, **kwargs)

    def get_avg_rating(self):
        average = self.user.received_ratings.aggregate(Avg("rating"))["rating__avg"]
        return average if average is not None else 0.0