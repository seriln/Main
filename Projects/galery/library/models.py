# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.

class Image(models.Model):
    name = models.CharField("Название", max_length=32)
    definition = models.CharField("Описание", max_length=256)
    image = models.ImageField(upload_to='images')
    def __unicode__(self):
        return u'%s %s' % (self.name,self.definition)
    def get_absolute_url(self):
        return "/library/authors/%i" % self.id
