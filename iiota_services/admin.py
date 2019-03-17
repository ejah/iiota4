#  Copyright (c) 2019. IIOTA (www.iiota.nl). All rights reserved.

from django.contrib import admin
from .models import IIotaService


@admin.register(IIotaService)
class IIotaServiceAdmin(admin.ModelAdmin):
    pass
