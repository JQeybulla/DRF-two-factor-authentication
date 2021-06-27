from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class CustomUser(AbstractUser):

    # two factor authentication fields
    two_factor_auth_status = models.BooleanField(default=False)
    two_factor_code = models.PositiveIntegerField(null=True, blank=True)
    tfa_code_reset = models.DateTimeField(default=timezone.now)
