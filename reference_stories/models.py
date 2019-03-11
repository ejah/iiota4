from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import activate


# Create your models here.
class MarketSegment(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)

    class Meta:
        verbose_name = 'Market Segment'
        verbose_name_plural = 'Market Segments'

    def __str__(self):
        return self.name


class ReferenceStory(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField()
    segment = models.ManyToManyField(MarketSegment, related_name='ReferenceStories')
    text = models.TextField()
    account = models.CharField(max_length=75)
    quote = models.TextField(max_length=200)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name_plural = "Reference Stories"
        verbose_name = "Reference Story"

    def segments(self):
        segment_classes = str(" ").join(item.name for item in self.segment.all())
        return segment_classes

    def get_absolute_url(self):
        return reverse("ref_stories:reference_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
