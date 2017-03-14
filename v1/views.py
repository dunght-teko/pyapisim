from time import sleep

from rest_framework.response import Response
from rest_framework.views import APIView
from soaplib.core.model.primitive import Any, String
from soaplib.core.service import rpc

from mysoap import SoapView
from v1.models import SimResponse


class RestService(APIView):
    def get(self, request, route):
        response = Response()
        try:
            sim_response = SimResponse.objects.get(route=route)
            response.status_code = sim_response.http_status_code
            response.content = sim_response.body
            headers = sim_response.headers.splitlines()
            for header in headers:
                key, value = header.split(':')
                response[key] = value
            sleep(sim_response.sleep_second)
        except SimResponse.DoesNotExist:
            return Response(data=u'This api does not exist')
        return response

    def post(self, request, route):
        response = Response()
        try:
            sim_response = SimResponse.objects.get(route=route)
            response.status_code = sim_response.http_status_code
            response.content = sim_response.body
            headers = sim_response.headers.splitlines()
            for header in headers:
                key, value = header.split(':')
                response[key] = value
            sleep(sim_response.sleep_second)
        except SimResponse.DoesNotExist:
            return Response(data=u'This api does not exist')
        return response


class SoapService(SoapView):
    __tns__ = 'http://api.sim.com:8998/soap/?wsdl'

    @rpc(String, _returns=String)
    def call(self, route):
        response = Response()
        try:
            sim_response = SimResponse.objects.get(route=route)
            response.status_code = sim_response.http_status_code
            response.content = sim_response.body
            headers = sim_response.headers.splitlines()
            for header in headers:
                key, value = header.split(':')
                response[key] = value
            sleep(sim_response.sleep_second)
        except SimResponse.DoesNotExist:
            return u'This api does not exist'
        return response.content


sim_soap_service = SoapService.as_view()
