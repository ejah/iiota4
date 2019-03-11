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
        for ref in ReferenceStory.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as first argument, a URL as
            # second argument and a (for this tree) unique id as third
            # argument.
            node = NavigationNode(
                ref.title,
                reverse('reference_detail', args=(ref.slug,)),
                ref.slug
            )
            nodes.append(node)
        return nodes
menu_pool.register_menu(ReferenceStoriesMenu) # register the menu.