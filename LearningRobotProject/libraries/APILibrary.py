import requests


class APILibrary:

    def __init__(self):
        pass

    def get_api_response(self, endpoint):
        response = requests.get(endpoint)
        return response
