# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    what is this 1 = models.TextField(max_length=255, null=True, blank=True)
    what is this 2 = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    test 1 = models.TextField(max_length=255, null=True, blank=True)
    test 2 = models.IntegerField(null=True, blank=True)
    test 3 = models.CharField(max_length=255, null=True, blank=True)
    test 4 = models.BooleanField()
    test 5 = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Product 2(models.Model):

    #__Product 2_FIELDS__
    testing 1 = models.TextField(max_length=255, null=True, blank=True)
    testing 2 = models.TextField(max_length=255, null=True, blank=True)

    #__Product 2_FIELDS__END

    class Meta:
        verbose_name        = _("Product 2")
        verbose_name_plural = _("Product 2")


class Product 3(models.Model):

    #__Product 3_FIELDS__
    hello 1 = models.IntegerField(null=True, blank=True)
    hello 2 = models.IntegerField(null=True, blank=True)

    #__Product 3_FIELDS__END

    class Meta:
        verbose_name        = _("Product 3")
        verbose_name_plural = _("Product 3")



#__MODELS__END
