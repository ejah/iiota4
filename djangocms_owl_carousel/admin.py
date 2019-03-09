from django.contrib import admin

from .models import OwlStyles, ReferenceStory, MarketSegment


# Register your models here.
@admin.register(OwlStyles)
class OwlStyleAdmin(admin.ModelAdmin):
    pass


@admin.register(ReferenceStory)
class ReferenceStoryAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketSegment)
class MarketSegmentAdmin(admin.ModelAdmin):
    pass
