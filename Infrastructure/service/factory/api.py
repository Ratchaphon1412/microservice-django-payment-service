import requests
import json

class APICall:
    
    def get(endpoints,data,header):
        response = requests.get(endpoints, data=json.dumps(data), headers=header)
        return response
    
    def post(endpoints,data,header):
        response = requests.post(endpoints, data=json.dumps(data), headers=header)
        return response
    
    def put(endpoints,data,header):
        response = requests.put(endpoints, data=json.dumps(data), headers=header)
        return response
    
    def delete(endpoints,data,header):
        response = requests.delete(endpoints, data=json.dumps(data), headers=header)
        return response