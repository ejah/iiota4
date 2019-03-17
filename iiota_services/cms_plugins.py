#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.
from cms.cms_plugins import CMSPlugin
from django.db import models
from .models import IIotaService
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


class IIotaServicePlugin(CMSPlugin):
    service = models.ForeignKey(IIotaService)

    # icon

    def __str__(self):
        return self.service.name + " - plugin"


@plugin_pool.register_plugin
class IIotaServiceBlockPlugin(CMSPluginBase):
    model = IIotaServicePlugin
    name = _("Service block plugin")
    render_template = "_service_block.html"
    cache = True
    allow_children = False
