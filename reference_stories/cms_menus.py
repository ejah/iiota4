#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from .models import ReferenceStory

class ReferenceStoriesMenu(CMSAttachMenu):
    name = _("Reference Story Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        nodes.append(NavigationNode(title='test', url="/", id='unieke_id'))
        for reference in ReferenceStory.objects.all():
            node = NavigationNode(
                title=reference.title,
                url=reverse('ref_stories:reference-detail', kwargs={'slug':reference.slug}),
                id=reference.slug
            )
            nodes.append(node)
        return nodes


# register the menu.
menu_pool.register_menu(ReferenceStoriesMenu)

