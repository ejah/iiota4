#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .cms_menus import IIotaServiceMenu


@apphook_pool.register
class IIotaServiceApp(CMSApp):
    app_name = "iiota_services"
    name = "IIota Services"

    # menu = [IIotaServiceMenu,]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["iiota_services.urls"]
