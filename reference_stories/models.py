#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class MarketSegment(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)

    class Meta:
        verbose_name = 'Market Segment'
        verbose_name_plural = 'Market Segments'

    def __str__(self):
        return self.name


class ReferenceStory(models.Model):
    title = models.CharField(verbose_name='Title of reference', max_length=100, null=False, blank=False)
    image = models.ImageField(verbose_name='Reference image')
    segment = models.ManyToManyField(MarketSegment, related_name='ReferenceStories')
    text = models.TextField(verbose_name='Reference body text')
    account = models.CharField(verbose_name='Account name', max_length=75)
    account_url = models.URLField(verbose_name="Account website", null=True)
    reference_name = models.CharField(verbose_name='Name of person for quote', max_length=75, null=True)
    quote = models.TextField(max_length=200, null=True)
    complexity = models.IntegerField(verbose_name='Project complexity', null=True)
    date_completed = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    challenge = models.TextField(verbose_name='The challenge of this project', null=True)
    businesscase = models.TextField(verbose_name='Describe the businesscase', null=True)
    solution = models.TextField(verbose_name='Describe the solution', null=True)
    challenge_image = models.ImageField(verbose_name='Challenge image', null=True)
    businesscase_image = models.ImageField(verbose_name='Businesscase image', null=True)
    solution_image = models.ImageField(verbose_name='Solution image', null=True)

    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = "Reference Stories"
        verbose_name = "Reference Story"

    def segments(self):
        segment_classes = str(" ").join(item.name for item in self.segment.all())
        return segment_classes

    def get_absolute_url(self):
        return reverse("ref_stories:reference-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
