import suds
import requests

def test_api(wsdl_url, api):
    client = suds.client.Client(wsdl_url, timeout=60)

    # functions = [m for m in client.wsdl.services[0].ports[0].methods]
    # count = 0
    # for function_name in functions:
    #     print function_name
    #     count+=1
    # print '\nNumber of services exposed: ', count
    
    service = client.service
    reply = service.call(api)
    print reply
    # return result

test_api('http://api.sim.com:8998/soap/?wsdl', 'example/api')