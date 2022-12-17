import requests

class VolleyMatch(object):
    def __init__(self, no):
        self.no = no

    def match(self):
        url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request=<Request Type='GetVolleyMatch' No='{}' />".format(self.no)
        headers = {'Accept': 'application/json'}

        response = requests.get(url, headers=headers)

        return response.json()