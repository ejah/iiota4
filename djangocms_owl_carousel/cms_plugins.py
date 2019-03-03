from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from djangocms_owl_carousel.models import CarouselHolder, CarouselItem

@plugin_pool.register_plugin
class CarouselHolderPlugin(CMSPluginBase):
    model = CarouselHolder
    name = _("Carousel Holder")
    render_template = 'carousel_holder.html'
    cache = False

@plugin_pool.register_plugin
class CarouselItemPlugin(CMSPluginBase):
    model = CarouselItem
    name = _("Carousel Item")
    render_template = 'carousel_item.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(CarouselItemPlugin, self).render(context, instance, placeholder)
        return context