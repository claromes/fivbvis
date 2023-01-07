import requests

class Article():
    def __init__(self):
        self.headers = {'Accept': 'application/json'}
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def get(self, no, fields=''):
        url = self.base_url + "<Request Type='GetArticle' No='{}' Fields='{}'/>".format(no, fields)

        response = requests.get(url, headers=self.headers)

        return response.json()