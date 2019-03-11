from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import ReferenceStoriesMenu


@apphook_pool.register
class ReferenceStoryApp(CMSApp):
    app_name = _("reference_stories")
    name = "Reference Stories"
    menu = [ReferenceStoriesMenu]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["reference_stories.urls"]