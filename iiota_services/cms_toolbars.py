#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import ugettext_lazy as _

from cms.utils.urlutils import admin_reverse


class IIotaServicesToolbar(CMSToolbar):

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu(
            key='iiota_services_cms_integration',
            verbose_name='IIota Services'
        )
        menu.add_sideframe_item(
            name=_('Services list'),
            url=admin_reverse('iiota_services_iiotaservice_changelist')
        )
        menu.add_sideframe_item(
            name=_('Add Service'),
            url=admin_reverse('iiota_services_iiotaservice_add')
        )


toolbar_pool.register(IIotaServicesToolbar)
