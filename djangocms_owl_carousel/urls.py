from django.conf.urls import include, url
from .views import ReferenceStoryView

urlpatterns = [
    url(r'^reference-stories/(?P<slug>[-\w]+)/$', ReferenceStoryView.as_view(), name='reference_detail'),
]