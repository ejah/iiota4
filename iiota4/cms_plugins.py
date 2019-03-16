from aldryn_newsblog.cms_plugins import NewsBlogFeaturedArticlesPlugin
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool

@plugin_pool.register_plugin
class IIotaFeaturedArticlesPlugin(NewsBlogFeaturedArticlesPlugin):
    render_template = 'iiota_featured_articles_block.html'
    name = _('Featured Articles Block')
