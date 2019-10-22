# -------- top-level imports ----------#
import uuid


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()



class AbandonedSignup(models.Model):
    """
    A model to capture the prospects who didn't complete the signup process.

    - on signup, check if the users email is here, if it is, remove it totally.
    
    - the purpose is to use a cron or celery task to notify them with goodies
    until they sign-up. In business terms, they get emailed every lead magnet we
    create.

    TODO:
        - connect these email with our newsletter for lead magnet goodie (Build trust and credibility)
    """
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):

    customer_id = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return "{}-{}".format(self.customer_id, self.user.get_full_name())

