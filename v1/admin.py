from django.contrib import admin

from models import SimGroup, SimResponse, SimGroupAdmin, SimResponseAdmin

admin.site.register(SimGroup, SimGroupAdmin)
admin.site.register(SimResponse, SimResponseAdmin)
