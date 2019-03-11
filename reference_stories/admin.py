from django.contrib import admin
from .models import ReferenceStory, MarketSegment

@admin.register(ReferenceStory)
class ReferenceStoryAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketSegment)
class MarketSegmentAdmin(admin.ModelAdmin):
    pass
