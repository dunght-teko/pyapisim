from time import sleep

from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from mysoap import SoapView
from v1.models import SimRequest, SimResponse


# from soaplib.core.model.primitive import Any, String
# from soaplib.core.service import rpc


class RestService(APIView):
    def dispatch(self, request, *args, **kwargs):
        route = kwargs['route']
        method = request.method
        sequence = request.GET.get('sequence', 1)

        response = Response()
        try:
            sim_request = SimRequest.objects.get(
                Q(method=method) | Q(method=SimRequest.METHOD_ANY),
                route=route
            )

            sim_response = SimResponse.objects.get(
                sequence=sequence,
                request=sim_request
            )

            headers = sim_response.headers.splitlines()
            for header in headers:
                key, value = header.split(':')
                response[key] = value

            response.status_code = sim_response.http_status_code
            response.content = sim_response.body

            sleep(sim_response.sleep_second)

        except SimRequest.DoesNotExist:
            return JsonResponse({
                'code': 'NOT_FOUND',
                'message': 'Request not found. HINT: check (METHOD, route).',
            }, status=status.HTTP_404_NOT_FOUND)

        except SimResponse.DoesNotExist:
            return JsonResponse({
                'code': 'NOT_FOUND',
                'message': 'Response not found. HINT: check (sequence).',
            }, status=status.HTTP_404_NOT_FOUND)

        return response

# class SoapService(SoapView):
#     __tns__ = 'http://api.sim.com:8998/soap/?wsdl'
#
#     @rpc(String, _returns=String)
#     def call(self, route):
#         response = Response()
#         try:
#             sim_response = SimResponse.objects.get(route=route)
#             response.status_code = sim_response.http_status_code
#             response.content = sim_response.body
#             headers = sim_response.headers.splitlines()
#             for header in headers:
#                 key, value = header.split(':')
#                 response[key] = value
#             sleep(sim_response.sleep_second)
#         except SimResponse.DoesNotExist:
#             return u'This api does not exist'
#         return response.content


# sim_soap_service = SoapService.as_view()
