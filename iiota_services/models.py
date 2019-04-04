#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField


class IIotaService(models.Model):
    name_first = models.CharField(max_length=25)
    name_second = models.CharField(max_length=25)
    image = FilerImageField(verbose_name='Service image',
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL,
                            )
    description = models.TextField(verbose_name='Beschrijving')
    slug = models.SlugField(editable=False, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def name(self):
        return self.name_first + " " + self.name_second

    def __str__(self):
        return self.name()

    def get_absolute_url(self):
        return reverse("iiota_services:service-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'IIota Service'
        verbose_name_plural = 'IIota Services'
