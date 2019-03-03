from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from djangocms_link.cms_plugins import LinkPlugin
from django.utils.translation import ugettext_lazy as _

from djangocms_owl_carousel.models import CarouselHolder, CarouselItem

@plugin_pool.register_plugin
class CarouselHolderPlugin(CMSPluginBase):
    model = CarouselHolder
    name = _("Carousel Holder")
    render_template = 'carousel_holder.html'
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(CarouselHolderPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class CarouselItemPlugin(CMSPluginBase):
    model = CarouselItem
    name = _("Carousel Item")
    render_template = 'carousel_item.html'
    cache = False
    require_parent = True
    allow_children = True
    child_classes = ['LinkPlugin',]

    def render(self, context, instance, placeholder):
        context = super(CarouselItemPlugin, self).render(context, instance, placeholder)
        return context