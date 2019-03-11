from django.conf.urls import include, url
from .views import ReferenceStoryView
from django.utils.translation import ugettext_lazy as _

app_name="ref_stories"
urlpatterns = [
    url(r'^reference-stories/(?P<slug>[-\w]+)/$', ReferenceStoryView.as_view(), name='reference_detail'),
]