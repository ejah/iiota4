#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.
from django.conf.urls import include, url
from .views import IIotaServiceDetailView, IIotaServiceListView
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

app_name = "iiota_services"
urlpatterns = [
    url(r'^$', IIotaServiceListView.as_view(), name='service-list'),
    url(r'^(?P<slug>[-\w]+)/$', IIotaServiceDetailView.as_view(), name='service-detail'),
]
