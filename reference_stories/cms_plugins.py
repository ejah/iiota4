from cms.cms_plugins import CMSPlugin
from django.db import models
from .models import ReferenceStory
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


class ReferenceStoryPlugin(CMSPlugin):
    story = models.ForeignKey(ReferenceStory)

    def __str__(self):
        return self.story.title + " - plugin"


@plugin_pool.register_plugin
class ReferenceStoryBlockPlugin(CMSPluginBase):
    model = ReferenceStoryPlugin
    name = _("Reference story block plugin")
    render_template = "_reference_story_block.html"
    cache = True
    allow_children = False
