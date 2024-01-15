import requests

class VolleyMatch():
    def __init__(self):
        self.headers = {'Accept': 'application/json'}
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def match(self, no):
        url = self.base_url + "<Request Type='GetVolleyMatch' No='{}' />".format(no)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def list(self,
            no_tournament,
            fields='City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName',
            filter=''):
        url = self.base_url + "<Request Type='GetVolleyMatchList' Fields='{}'><Filter {} NoTournament='{}' /></Request>".format(fields, filter, no_tournament)

        response = requests.get(url, headers=self.headers)

        return response.json()