# -*- coding: utf-8 -*-

from django.db import models

class Prototype(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True, db_index=True)
    
    class Meta:
        abstract = True

class Zone(Prototype):
    pass

class Domain(Prototype):
    zone = models.ForeignKey(Zone)
    registrer_date = models.DateField(null=False)
    release_date = models.DateField(null=False)
    registrator = models.CharField(max_length=128)