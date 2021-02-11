import requests
import json


def create_resource():
    new_data = {
        'techie_id': 1019,
        'techie_name': 'hish',
        'techie_skill': 'Scala',
        'techie_profile': 'Scala dev',
        'techie_salary': 100000
    }
    try:
        resp = requests.post('http://127.0.0.1:8000/rest_api/api/', data=json.dumps(new_data),timeout=0.000002)
        print(resp.status_code)
        print(resp.json())
    except requests.exceptions.ReadTimeout:
        print('Time out')


create_resource()


# def getresource():
#     new_data = {
#         'techie_id': 1008,
#         'techie_name': 'Satish',
#         'techie_skill': 'Redhat',
#         'techie_profile': 'Scala dev',
#         'techie_salary': 90000
#     }
#     try:
#         resp = requests.post('http://127.0.0.1:8000/rest_api/api/', data=json.dumps(new_data),
#                              timeout=10)
#     except requests.exceptions.ReadTimeout:
#         print('Time out')
#
#
# getresource()
