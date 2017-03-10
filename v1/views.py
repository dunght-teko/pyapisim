from time import sleep

from django.http.response import HttpResponse

from v1.models import SimResponse


def display_sim_response(request, route=None):
    response = HttpResponse()
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
        return HttpResponse(content=u'This api does not exist')
    return response
