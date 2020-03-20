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


class SimRequest(models.Model):
    METHOD_ANY = 'any'
    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_PUT = 'PUT'
    METHOD_DELETE = 'DELETE'
    METHOD_OPTION = 'OPTION'

    METHOD_CHOICES = [
        (METHOD_ANY, '<any>'),
        (METHOD_GET, 'GET'),
        (METHOD_POST, 'POST'),
        (METHOD_PUT, 'PUT'),
        (METHOD_DELETE, 'DELETE'),
        (METHOD_OPTION, 'OPTION'),
    ]
    group = models.ForeignKey(SimGroup)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES, default=METHOD_ANY, null=False, blank=False)
    route = models.CharField(max_length=50, null=False, help_text=u'Route on URL of Simulator link')
    name = models.CharField(max_length=150, null=False, help_text=u'Name of simulated response')
    description = models.TextField(blank=True, max_length=500, help_text=u'Description')

    class Meta:
        unique_together = ('route', 'method',)

    def __str__(self):
        return '#%s %s' % (self.id, self.name)


class SimResponse(models.Model):
    request = models.ForeignKey(SimRequest)
    sequence = models.IntegerField(default=1, help_text=u'Unique by request')
    headers = models.TextField(blank=True, help_text=u'Headers fore request')
    sleep_second = models.PositiveSmallIntegerField(default=0, help_text=u'Seconds')
    http_status_code = models.PositiveSmallIntegerField(
        default=200, help_text=u'HTTP status code of response', choices=HTTP_STATUS_CODE)
    body = models.TextField(null=False, help_text=u'Body of response')

    class Meta:
        unique_together = ('request', 'sequence',)


class SimRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'method', 'route')
    list_select_related = True
    list_filter = ('group__name',)
    list_display_links = ('name', 'route')
    search_fields = ('name', 'description')


class SimResponseAdmin(admin.ModelAdmin):
    list_display = ('request', 'sequence', 'http_status_code', 'sleep_second')
    ordering = ('request', 'sequence')
