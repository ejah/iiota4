from django.test import TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_pool import plugin_pool
from cms.plugin_rendering import ContentRenderer

from .cms_plugins import CarouselHolderPlugin, CarouselItemPlugin
# from .models import CarouselHolder, CarouselItem


class CarouselHolderPluginTests(TestCase):

    def setUp(self):
            if CarouselHolderPlugin in plugin_pool.registered_plugins:
                plugin_pool.unregister_plugin(CarouselHolderPlugin)


    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            CarouselHolderPlugin,
            'nl',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('key', context)
        self.assertEqual(context['key'], 'value')

    # def test_plugin_html(self):
    #     placeholder = Placeholder.objects.create(slot='test')
    #     model_instance = add_plugin(
    #         placeholder,
    #         CarouselHolderPlugin,
    #         'nl',
    #     )
    #     renderer = ContentRenderer(request=RequestFactory())
    #     html = renderer.render_plugin(model_instance, {})
    #     self.assertEqual(html, '<section class="main_slider"></section>')
    #
