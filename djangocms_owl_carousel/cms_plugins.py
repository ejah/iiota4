from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
# from cms.models.pluginmodel import CMSPlugin
# from djangocms_link.cms_plugins import LinkPlugin
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin import StackedInline
from djangocms_owl_carousel.models import CarouselHolder, CarouselItem, OwlCarouselHolder, OwlCarouselItem, OWL_STYLE_CHOICES, OwlStyles



class OwlStyleStackedInline(StackedInline):
    model = OwlStyles


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
    # inlines = [OwlStyleStackedInline,]
    # child_classes = ['OwlCarouselItem',]

    def get_render_template(self, context, instance, placeholder):
        for child_instance in instance.child_plugin_instances:
            child_instance.render_template = instance.style.item_template
        return instance.style.main_template

    # def render(self, context, instance, placeholder):
    #     context = super(OwlCarouselHolderPlugin, self).render(context, instance, placeholder)
    #     return context


@plugin_pool.register_plugin
class OwlCarouselItemPlugin(CMSPluginBase):
    model = OwlCarouselItem
    name = _("Owl Carousel Item")
    render_template = 'owl_carousel_item.html'
    cache = False
    require_parent = True
    allow_children = True
    child_classes = ['LinkPlugin', ]

    # def get_render_template(self, context, instance, placeholder):
    #     return instance.parent.style.item_template

    def render(self, context, instance, placeholder):
        context = super(OwlCarouselItemPlugin, self).render(context, instance, placeholder)
        return context
