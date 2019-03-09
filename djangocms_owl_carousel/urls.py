from django.conf.urls import include, url

from django.conf.urls.i18n import i18n_patterns
from .views import ReferenceStoryView

urlpatterns = i18n_patterns(
    url(r'^reference-stories/(?P<slug>[-\w]+)/$', ReferenceStoryView.as_view(), name='reference_detail'),
)