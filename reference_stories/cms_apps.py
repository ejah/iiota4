from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .cms_menus import ReferenceStoriesMenu


@apphook_pool.register
class ReferenceStoryApp(CMSApp):
    app_name = "ref_stories"
    name = "Reference Stories"
    # menu = [ReferenceStoriesMenu]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["reference_stories.urls"]
