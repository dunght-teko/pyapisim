from django.contrib import admin
from django.db import models

from apisimulator import HTTP_STATUS_CODE


# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
class SimGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SimGroupAdmin(admin.ModelAdmin):
    pass


class SimResponse(models.Model):
    group = models.ForeignKey(SimGroup)
    route = models.CharField(max_length=50, null=False, unique=True, help_text=u'Route on URL of Simulator link')
    name = models.CharField(max_length=150, null=False, help_text=u'Name of simulated response')
    description = models.TextField(blank=True, max_length=500, help_text=u'Description')
    headers = models.TextField(blank=True, help_text=u'Headers fore request')
    sleep_second = models.PositiveSmallIntegerField(default=0, help_text=u'Seconds')
    http_status_code = models.PositiveSmallIntegerField(default=200, help_text=u'HTTP status code of response', choices=HTTP_STATUS_CODE)
    body = models.TextField(null=False, help_text=u'Body of response')


class SimResponseAdmin(admin.ModelAdmin):
    list_display = ('group', 'name', 'route', 'sleep_second', 'description')
    list_select_related = True
    list_filter = ('group__name',)
    list_display_links = ('name', 'route')
    search_fields = ('name', 'description')
