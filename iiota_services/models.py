#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class IIotaService(models.Model):
    name_first = models.CharField(max_length=25)
    name_second = models.CharField(max_length=25)
    image = models.ImageField(verbose_name='Service afbeelding')
    description = models.TextField(verbose_name='Beschrijving')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def name(self):
        return self.name_first + " " + self.name_second

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("iiota_services:service-detail", kwargs={"slug": self.slug})
