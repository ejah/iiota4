from cms.cms_plugins import CMSPlugin
from django.db import models
# from django.utils.translation import ugettext_lazy as _

SERVICE_STYLE_ONE = 1
SERVICE_STYLE_TWO = 2
SERVICE_STYLE_THREE = 3
SERVICE_STYLE_FOUR = 4
PORTFOLIO_STYLE_TWO = 5
TESTIMONIALS_STYLE_ONE = 6
TESTIMONIALS_STYLE_TWO = 7
TESTIMONIALS_STYLE_THREE = 8
TESTIMONIALS_STYLE_FOUR = 9

OWL_STYLE_CHOICES = (
    (SERVICE_STYLE_ONE, 'Service style one'),
    (SERVICE_STYLE_TWO, 'Service style two'),
    (SERVICE_STYLE_THREE, 'Service style three'),
    (SERVICE_STYLE_FOUR, 'Service style four'),
    (PORTFOLIO_STYLE_TWO, 'Portfolio style two'),
    (TESTIMONIALS_STYLE_ONE, 'Testimonials, style one'),
    (TESTIMONIALS_STYLE_TWO, 'Testimonials style two'),
    (TESTIMONIALS_STYLE_THREE, 'Testimonials style three'),
    (TESTIMONIALS_STYLE_FOUR, 'Testimonials style four'),
)

class OwlStyles(models.Model):
    title = models.CharField(max_length=30, null=False)
    main_template = models.CharField(max_length=100)
    item_template = models.CharField(max_length=100)

    def __str__(self):
        return self.title


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
    style = models.ForeignKey(OwlStyles, on_delete=None)


class OwlCarouselItem(CMSPlugin):
    INDUSTRIO_ICON_EMAILS_INTERFACE_DOWNLOAD_SYMBOL = 'industrio-icon-emails-interface-download-symbol'
    INDUSTRIO_ICON_PDF = 'industrio-icon-pdf'
    INDUSTRIO_ICON_MENU = 'industrio-icon-menu'
    INDUSTRIO_ICON_NEXT = 'industrio-icon-next'
    INDUSTRIO_ICON_COFFEE_CUP = 'industrio-icon-coffee-cup'
    INDUSTRIO_ICON_TEAM = 'industrio-icon-team'
    INDUSTRIO_ICON_CHILD = 'industrio-icon-child'
    INDUSTRIO_ICON_PLAY_BUTTON = 'industrio-icon-play-button'
    INDUSTRIO_ICON_WIND_ENGINE = 'industrio-icon-wind-engine'
    INDUSTRIO_ICON_SETTINGS_1 = 'industrio-icon-settings-1'
    INDUSTRIO_ICON_DELIVERY_TRUCK = 'industrio-icon-delivery-truck'
    INDUSTRIO_ICON_SUPPORT = 'industrio-icon-support'
    INDUSTRIO_ICON_SECURE_SHIELD = 'industrio-icon-secure-shield'
    INDUSTRIO_ICON_ATOMIC = 'industrio-icon-atomic'
    INDUSTRIO_ICON_PLANT = 'industrio-icon-plant'
    INDUSTRIO_ICON_SETTINGS = 'industrio-icon-settings'
    INDUSTRIO_ICON_SAFETY = 'industrio-icon-safety'
    INDUSTRIO_ICON_DROP_OF_LIQUID = 'industrio-icon-drop-of-liquid'
    INDUSTRIO_ICON_SCYTHE = 'industrio-icon-scythe'
    INDUSTRIO_ICON_FACTORY_1 = 'industrio-icon-factory-1'
    INDUSTRIO_ICON_GREEN_ENERGY = 'industrio-icon-green-energy'
    INDUSTRIO_ICON_INNOVATION = 'industrio-icon-innovation'
    INDUSTRIO_ICON_GAS_STATION_1 = 'industrio-icon-gas-station-1'
    INDUSTRIO_ICON_LAYERS = 'industrio-icon-layers'
    INDUSTRIO_ICON_ATOM = 'industrio-icon-atom'
    INDUSTRIO_ICON_FLASKS = 'industrio-icon-flasks'
    INDUSTRIO_ICON_GAS_STATION = 'industrio-icon-gas-station'
    INDUSTRIO_ICON_GAS_PIPE = 'industrio-icon-gas-pipe'
    INDUSTRIO_ICON_TOWER = 'industrio-icon-tower'
    INDUSTRIO_ICON_VALVE = 'industrio-icon-valve'
    INDUSTRIO_ICON_INDUSTRY = 'industrio-icon-industry'
    INDUSTRIO_ICON_WORKER = 'industrio-icon-worker'
    INDUSTRIO_ICON_ENVELOPE = 'industrio-icon-envelope'
    INDUSTRIO_ICON_CLOCK = 'industrio-icon-clock'
    INDUSTRIO_ICON_PHONE_CALL = 'industrio-icon-phone-call'
    INDUSTRIO_ICON_RIGHT_QUOTE = 'industrio-icon-right-quote'


    OWL_ICON_CHOICES = (
        (INDUSTRIO_ICON_EMAILS_INTERFACE_DOWNLOAD_SYMBOL, 'Download'),
        (INDUSTRIO_ICON_PDF, 'PDF'),
        (INDUSTRIO_ICON_MENU, 'Menu'),
        (INDUSTRIO_ICON_NEXT, 'Next'),
        (INDUSTRIO_ICON_COFFEE_CUP, 'Coffee'),
        (INDUSTRIO_ICON_TEAM, 'Team'),
        (INDUSTRIO_ICON_CHILD, 'Child'),
        (INDUSTRIO_ICON_PLAY_BUTTON, 'Play'),
        (INDUSTRIO_ICON_WIND_ENGINE, 'Wind engine'),
        (INDUSTRIO_ICON_SETTINGS_1, 'Settings 1'),
        (INDUSTRIO_ICON_DELIVERY_TRUCK, 'Truck'),
        (INDUSTRIO_ICON_SUPPORT, 'Support'),
        (INDUSTRIO_ICON_SECURE_SHIELD, 'Secure'),
        (INDUSTRIO_ICON_ATOMIC, 'Atomic'),
        (INDUSTRIO_ICON_PLANT, 'Plant'),
        (INDUSTRIO_ICON_SETTINGS, 'Settings'),
        (INDUSTRIO_ICON_SAFETY, 'Safety'),
        (INDUSTRIO_ICON_DROP_OF_LIQUID, 'Drop'),
        (INDUSTRIO_ICON_SCYTHE, 'Scythe'),
        (INDUSTRIO_ICON_FACTORY_1, 'Factory-1'),
        (INDUSTRIO_ICON_GREEN_ENERGY, 'Green energy'),
        (INDUSTRIO_ICON_INNOVATION, 'Innovation'),
        (INDUSTRIO_ICON_GAS_STATION_1, 'Gas station 1'),
        (INDUSTRIO_ICON_LAYERS, 'Layers'),
        (INDUSTRIO_ICON_ATOM, 'Atom'),
        (INDUSTRIO_ICON_FLASKS, 'Flasks'),
        (INDUSTRIO_ICON_GAS_STATION, 'Gas stations'),
        (INDUSTRIO_ICON_GAS_PIPE, 'Gas pipe'),
        (INDUSTRIO_ICON_TOWER, 'Tower'),
        (INDUSTRIO_ICON_VALVE, 'Valve'),
        (INDUSTRIO_ICON_INDUSTRY, 'Industry'),
        (INDUSTRIO_ICON_WORKER, 'Worker'),
        (INDUSTRIO_ICON_ENVELOPE, 'Envelope'),
        (INDUSTRIO_ICON_CLOCK, 'Clock'),
        (INDUSTRIO_ICON_PHONE_CALL, 'Phone call'),
        (INDUSTRIO_ICON_RIGHT_QUOTE, 'Right quote'),)

    image = models.ImageField(verbose_name='Thumb image', null=True)
    alt_text = models.CharField(max_length=100, null=True)
    style = models.ForeignKey(OwlStyles, on_delete=None)

    icon = models.CharField(max_length=35, choices=OWL_ICON_CHOICES)
    title = models.CharField(max_length=75, null=True)
    text = models.TextField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "OWL Carousel Items"
        verbose_name = "OWL Carousel Item"
