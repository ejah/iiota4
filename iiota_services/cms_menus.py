#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.
from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from .models import IIotaService


class IIotaServiceMenu(CMSAttachMenu):
    name = _("Services Menu")  # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []

        nodes.append(NavigationNode(title='test', url="/", id='unieke_id'))
        for service in IIotaService.objects.all():
            node = NavigationNode(
                title=service.name_first,
                url=reverse('iiota_services:service-detail', kwargs={'slug': service.slug}),
                id=service.slug
            )
            nodes.append(node)
        return nodes


# register the menu.
menu_pool.register_menu(IIotaServiceMenu)
