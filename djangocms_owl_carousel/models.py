from cms.cms_plugins import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CarouselHolder(CMSPlugin):
    pass

class CarouselItem(CMSPlugin):
    image_thumb = models.ImageField(verbose_name='Thumb image', null=True)
    slide_index = models.IntegerField(verbose_name='slide_index', null=False, default=1)

    class Meta:
        verbose_name_plural = "Carousel Items"
        verbose_name = "Carousel Item"