from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
# from cms.models.pluginmodel import CMSPlugin
# from djangocms_link.cms_plugins import LinkPlugin
from django.utils.translation import ugettext_lazy as _

from djangocms_owl_carousel.models import CarouselHolder, CarouselItem, OwlCarouselHolder, OwlCarouselItem


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
    child_classes = ['LinkPlugin', ]

    def render(self, context, instance, placeholder):
        context = super(CarouselItemPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class OwlCarouselHolderPlugin(CMSPluginBase):
    model = OwlCarouselHolder
    name = _("Owl Carousel Holder")
    render_template = 'owl_carousel_holder.html'
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(OwlCarouselHolderPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class OwlCarouselItemPlugin(CMSPluginBase):
    model = OwlCarouselItem
    name = _("Carousel Item")
    render_template = 'owl_carousel_item.html'
    cache = False
    require_parent = True
    allow_children = True
    child_classes = ['LinkPlugin', ]

    def render(self, context, instance, placeholder):
        context = super(OwlCarouselItemPlugin, self).render(context, instance, placeholder)
        return context
