# -*- coding: utf-8 -*-
'''
documentation in http://soaplib.github.com/soaplib/2_0/
'''
from soaplib.core import Application
from soaplib.core.service import DefinitionBase
from soaplib.core.server import wsgi

from django.http import HttpResponse

# the class with actual web methods

# the class which acts as a wrapper between soaplib WSGI functionality and Django
class DjangoSoapApp(wsgi.Application):
    def __call__(self, request):
        # wrap the soaplib response into a Django response object
        django_response = HttpResponse()
        def start_response(status, headers):
            status, reason = status.split(' ', 1)
            django_response.status_code = int(status)
            for header, value in headers:
                django_response[header] = value
        response = super(DjangoSoapApp, self).__call__(request.META, start_response)
        django_response.content = '\n'.join(response)
        return django_response

class SoapView(DefinitionBase):
    @classmethod
    def as_view(cls):
        soap_application = Application([cls], __name__)
        return DjangoSoapApp(soap_application)

