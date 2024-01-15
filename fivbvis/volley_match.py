import requests

FIELDS = 'City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName'

class VolleyMatch():
    def __init__(self):
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def match(self, no, response_format='xml'):
        url = self.base_url + f"<Request Type='GetVolleyMatch' No='{no}' />"

        if response_format != 'json' and response_format != 'xml':
            raise ValueError(f'{response_format}: The provided value is not accepted.')

        headers = {'Accept': f'application/{response_format}'}

        response = requests.get(url, headers=headers)

        if response_format == 'xml':
            return response.text
        elif response_format == 'json':
            return response.json()

    def list(self, no_tournament, fields=FIELDS, filters='', response_format='xml'):
        url = self.base_url + f"<Request Type='GetVolleyMatchList' Fields='{fields}'><Filter {filters} NoTournament='{no_tournament}' /></Request>"

        if response_format != 'json' and response_format != 'xml':
            raise ValueError(f'{response_format}: The provided value is not accepted.')

        headers = {'Accept': f'application/{response_format}'}

        response = requests.get(url, headers=headers)

        if response_format == 'xml':
            return response.text
        elif response_format == 'json':
            return response.json()