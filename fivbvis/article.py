import requests

class Article():
    def __init__(self):
        self.headers = {'Accept': 'application/json'}
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def get(self, no, fields=''):
        url = self.base_url + "<Request Type='GetArticle' No='{}' Fields='{}'/>".format(no, fields)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def list(self, fields, filter='', tags=''):
        url = self.base_url + "<Request Type='GetArticleList' Fields='{}'><Filter>'{}'<Tags>{}</Tags></Filter></Request>".format(fields, filter, tags)

        response = requests.get(url, headers=self.headers)

        return response.json()