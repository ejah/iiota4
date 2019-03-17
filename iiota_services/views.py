#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from django.views.generic import DetailView, ListView
from .models import IIotaService


class IIotaServiceListView(ListView):
    model = IIotaService
    template_name = "_iiota_service_list.html"
    context_object_name = 'services_list'


class IIotaServiceDetailView(DetailView):
    model = IIotaService
    template_name = "_iiota_service_detail.html"
