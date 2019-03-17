#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import ugettext_lazy as _

from cms.utils.urlutils import admin_reverse


class ReferenceStoryToolbar(CMSToolbar):

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu(
            key='ref_stories_cms_integration',
            verbose_name='Reference Stories'
        )
        menu.add_sideframe_item(
            name=_('Story list'),
            url=admin_reverse('reference_stories_referencestory_changelist')
        )
        menu.add_sideframe_item(
            name=_('Add Story'),
            url=admin_reverse('reference_stories_referencestory_add')
        )


toolbar_pool.register(ReferenceStoryToolbar)
