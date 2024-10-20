import random
from django.db import models
from django.contrib.auth.models import User
from .constants import RELIGION_CHOICES, ACCOUNT_TYPE_CHOICES

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=12, null=True, blank=True, default='0')
    mobile_no = models.CharField(max_length=12)
    nid = models.CharField(max_length=12, unique=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    age = models.CharField(max_length=5)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    monthly_income = models.CharField(max_length=10)
    account_no = models.CharField(max_length=12, unique=True)
    religion = models.CharField(max_length=30, choices=RELIGION_CHOICES, null=True, blank=True)
    account_type = models.CharField(max_length=30, choices=ACCOUNT_TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        if not self.account_no:
            self.account_no = self.generate_unique_account_no()
        super().save(*args, **kwargs)

    def generate_unique_account_no(self):
        while True:
            account_no = ''.join(random.choices('0123456789', k=10))
            if not Customer.objects.filter(account_no=account_no).exists():
                return account_no


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    image = models.CharField(max_length=255, null=True, blank=True)
    nid = models.CharField(max_length=12, unique=True)
    age = models.CharField(max_length=5)
    religion = models.CharField(max_length=30, choices=RELIGION_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
