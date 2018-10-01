# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25,blank=False)
    email=models.CharField(max_length=30,blank=False)
    subject=models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.name