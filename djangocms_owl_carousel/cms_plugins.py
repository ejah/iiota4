from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin import StackedInline
from djangocms_owl_carousel.models import CarouselHolder, CarouselItem, OwlCarouselHolder, OwlCarouselItem, \
    OWL_STYLE_CHOICES, OwlStyles
from reference_stories.cms_plugins import ReferenceStoryPlugin


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
    cache = False
    allow_children = True


    def get_render_template(self, context, instance, placeholder):
        # probeer een style item aan de context toe te voegen.
        context['item_style'] = instance.style.item_template
        return instance.style.main_template



@plugin_pool.register_plugin
class OwlCarouselItemPlugin(CMSPluginBase):
    model = OwlCarouselItem
    name = _("Owl Carousel Item")
    render_template = 'owl_carousel_item.html'
    cache = False
    require_parent = True
    allow_children = True
    child_classes = ['LinkPlugin', ]

    def get_render_template(self, context, instance, placeholder):
        testje = context['item_style']
        return testje
        # return instance.style.item_template

# from aldryn_newsblog.cms_plugins import NewsBlogFeaturedArticlesPlugin
# from django.utils.translation import ugettext_lazy as _
#
# class IIotaFeaturedArticlesPlugin(NewsBlogFeaturedArticlesPlugin):
#     render_template = 'iiota_featured_articles_block.html'
#     name = _('Featured Articles Block')



