#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .cms_menus import ReferenceStoriesMenu


@apphook_pool.register
class ReferenceStoryApp(CMSApp):
    app_name = "ref_stories"
    name = _("Reference Stories")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["reference_stories.urls"]

    # def get_menus(self, page=None, language=None, **kwargs):
    #     return self.menu
