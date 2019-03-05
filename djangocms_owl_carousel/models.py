from cms.cms_plugins import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CarouselHolder(CMSPlugin):
    pass


class CarouselItem(CMSPlugin):
    image_thumb = models.ImageField(verbose_name='Thumb image', null=True)
    slide_index = models.IntegerField(verbose_name='slide_index', null=False, default=1)
    caption = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "Carousel Items"
        verbose_name = "Carousel Item"


class OwlCarouselHolder(CMSPlugin):
    section_style = models.CharField(max_length=75, default='service-style-two', null=True)
    style = models.CharField(max_length=75, default='service-carousel-style-two', null=True)


class OwlCarouselItem(CMSPlugin):

    INDUSTRIO_ICON_EMAILS_INTERFACE_DOWNLOAD_SYMBOL = 'Download'
    INDUSTRIO_ICON_PDF = 'PDF'
    INDUSTRIO_ICON_MENU = 'Menu'
    INDUSTRIO_ICON_NEXT = 'Next'
    INDUSTRIO_ICON_COFFEE_CUP = 'Coffee'
    INDUSTRIO_ICON_TEAM = 'Team'
    INDUSTRIO_ICON_CHILD = 'Child'
    INDUSTRIO_ICON_PLAY_BUTTON = 'Play'
    INDUSTRIO_ICON_WIND_ENGINE = 'Wind engine'
    INDUSTRIO_ICON_SETTINGS_1 = 'Settings 1'
    INDUSTRIO_ICON_DELIVERY_TRUCK = 'Truck'
    INDUSTRIO_ICON_SUPPORT = 'Support'
    INDUSTRIO_ICON_SECURE_SHIELD = 'Secure'
    INDUSTRIO_ICON_ATOMIC = 'Atomic'
    INDUSTRIO_ICON_PLANT = 'Plant'
    INDUSTRIO_ICON_SETTINGS = 'Settings'
    INDUSTRIO_ICON_SAFETY = 'Safety'
    INDUSTRIO_ICON_DROP_OF_LIQUID = 'Drop'
    INDUSTRIO_ICON_SCYTHE = 'Scythe'
    INDUSTRIO_ICON_FACTORY_1 = 'Factory-1'
    INDUSTRIO_ICON_GREEN_ENERGY = 'Green energy'
    INDUSTRIO_ICON_INNOVATION = 'Innovation'
    INDUSTRIO_ICON_GAS_STATION_1 = 'Gas station 1'
    INDUSTRIO_ICON_LAYERS = 'Layers'
    INDUSTRIO_ICON_ATOM = 'Atom'
    INDUSTRIO_ICON_FLASKS = 'Flasks'
    INDUSTRIO_ICON_GAS_STATION = 'Gas stations'
    INDUSTRIO_ICON_GAS_PIPE = 'Gas pipe'
    INDUSTRIO_ICON_TOWER = 'Tower'
    INDUSTRIO_ICON_VALVE = 'Valve'
    INDUSTRIO_ICON_INDUSTRY = 'Industry'
    INDUSTRIO_ICON_WORKER = 'Worker'
    INDUSTRIO_ICON_ENVELOPE = 'Envelope'
    INDUSTRIO_ICON_CLOCK = 'Clock'
    INDUSTRIO_ICON_PHONE_CALL = 'Phone call'
    INDUSTRIO_ICON_RIGHT_QUOTE = 'Right quote'

    OWL_ICON_CHOICES = (
        (INDUSTRIO_ICON_EMAILS_INTERFACE_DOWNLOAD_SYMBOL, 'industrio_ICON_emails-interface-download-symbol'),
        (INDUSTRIO_ICON_PDF, 'industrio_ICON_pdf'),
        (INDUSTRIO_ICON_MENU, 'industrio_ICON_menu'),
        (INDUSTRIO_ICON_NEXT, 'industrio_ICON_next'),
        (INDUSTRIO_ICON_COFFEE_CUP, 'industrio_ICON_coffee-cup'),
        (INDUSTRIO_ICON_TEAM, 'industrio_ICON_team'),
        (INDUSTRIO_ICON_CHILD, 'industrio_ICON_child'),
        (INDUSTRIO_ICON_PLAY_BUTTON, 'industrio_ICON_play-button'),
        (INDUSTRIO_ICON_WIND_ENGINE, 'industrio_ICON_wind-engine'),
        (INDUSTRIO_ICON_SETTINGS_1, 'industrio_ICON_settings-1'),
        (INDUSTRIO_ICON_DELIVERY_TRUCK, 'industrio_ICON_delivery-truck'),
        (INDUSTRIO_ICON_SUPPORT, 'industrio_ICON_support'),
        (INDUSTRIO_ICON_SECURE_SHIELD, 'industrio_ICON_secure-shield'),
        (INDUSTRIO_ICON_ATOMIC, 'industrio_ICON_atomic'),
        (INDUSTRIO_ICON_PLANT, 'industrio_ICON_plant'),
        (INDUSTRIO_ICON_SETTINGS, 'industrio_ICON_settings'),
        (INDUSTRIO_ICON_SAFETY, 'industrio_ICON_safety'),
        (INDUSTRIO_ICON_DROP_OF_LIQUID, 'industrio_ICON_drop-of-liquid'),
        (INDUSTRIO_ICON_SCYTHE, 'industrio_ICON_scythe'),
        (INDUSTRIO_ICON_FACTORY_1, 'industrio_ICON_factory-1'),
        (INDUSTRIO_ICON_GREEN_ENERGY, 'industrio_ICON_green-energy'),
        (INDUSTRIO_ICON_INNOVATION, 'industrio_ICON_innovation'),
        (INDUSTRIO_ICON_GAS_STATION_1, 'industrio_ICON_gas-station-1'),
        (INDUSTRIO_ICON_LAYERS, 'industrio_ICON_layers'),
        (INDUSTRIO_ICON_ATOM, 'industrio_ICON_atom'),
        (INDUSTRIO_ICON_FLASKS, 'industrio_ICON_flasks'),
        (INDUSTRIO_ICON_GAS_STATION, 'industrio_ICON_gas-station'),
        (INDUSTRIO_ICON_GAS_PIPE, 'industrio_ICON_gas-pipe'),
        (INDUSTRIO_ICON_TOWER, 'industrio_ICON_tower'),
        (INDUSTRIO_ICON_VALVE, 'industrio_ICON_valve'),
        (INDUSTRIO_ICON_INDUSTRY, 'industrio_ICON_industry'),
        (INDUSTRIO_ICON_WORKER, 'industrio_ICON_worker'),
        (INDUSTRIO_ICON_ENVELOPE, 'industrio_ICON_envelope'),
        (INDUSTRIO_ICON_CLOCK, 'industrio_ICON_clock'),
        (INDUSTRIO_ICON_PHONE_CALL, 'industrio_ICON_phone-call'),
        (INDUSTRIO_ICON_RIGHT_QUOTE, 'industrio_ICON_right-quote'))

    image = models.ImageField(verbose_name='Thumb image', null=True)
    alt_text = models.CharField(max_length=100, null=True)
    style = models.CharField(max_length=75, default='single-service-style-two', null=True)
    icon = models.CharField(max_length=20, choices=OWL_ICON_CHOICES)
    title = models.CharField(max_length=75, null=True)
    text = models.TextField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "OWL Carousel Items"
        verbose_name = "OWL Carousel Item"
