from django.contrib import admin

from v1.models import SimGroup, SimGroupAdmin, SimRequest, SimRequestAdmin, SimResponse, SimResponseAdmin


admin.site.register(SimGroup, SimGroupAdmin)
admin.site.register(SimRequest, SimRequestAdmin)
admin.site.register(SimResponse, SimResponseAdmin)
