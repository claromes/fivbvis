import requests

class VolleyMatch():
    def __init__(self):
        self.headers = {'Accept': 'application/json'}
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def match(self, no):
        url = self.base_url + f"<Request Type='GetVolleyMatch' No='{no}' />"

        response = requests.get(url, headers=self.headers)

        return response.json()

    def list(self,
            no_tournament,
            fields='City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName',
            filters=''):
        url = self.base_url + f"<Request Type='GetVolleyMatchList' Fields='{fields}'><Filter {filters} NoTournament='{no_tournament}' /></Request>"

        response = requests.get(url, headers=self.headers)

        return response.json()