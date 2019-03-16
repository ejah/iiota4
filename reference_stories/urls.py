from django.conf.urls import include, url
from .views import ReferenceStoryView, ReferenceStoryListView
from django.utils.translation import ugettext_lazy as _

app_name="ref_stories"
urlpatterns = [
    url(r'^$', ReferenceStoryListView.as_view(), name='reference-list'),
    url(r'^(?P<slug>[-\w]+)/$', ReferenceStoryView.as_view(), name='reference-detail'),
]