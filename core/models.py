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

    PLANS = (
        ('Free', 'Free'),
        ('Mini', 'Mini'),
        ('Biggie', 'Biggie'),
        ('Maxxie', 'Maxxie')
    )
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_plan = models.CharField(max_length=100, choices=PLANS, blank=True)

    # current_plan_expires = models.DateTimeField() # 30 days after expiry date


    # def user_quota(self, user_plan):
    #     "calls set_quota to know the user quota so it can be subtracted from request"
    #     pass

    # def _set_quota(self, plan):
    #     "this method is called after the user makes payment for a plan"
    #     if plan == 'Free':
    #         self.QUOTA = 1
    #     elif plan == 'Mini':
    #         self.QUOTA = 10
    #     elif plan == 'Biggie':
    #         self.QUOTA = 20
    #     elif plan == 'Maxxie':
    #         self.QUOTA = 30
    #     else:
    #         self.QUOTA = self.QUOTA

    #     return self.QUOTA

