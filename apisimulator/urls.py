"""apisimulator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from v1 import views as v1_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest/(?P<route>.+)$', v1_views.RestService.as_view(), name='http_response'),
    # url(r'^soap/$', v1_views.SoapSimView.as_view()),
    # url(r'^soap/$', v1_views.sim_soap_service, name='soap_server_error_code'),
]
