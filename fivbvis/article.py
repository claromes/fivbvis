import requests

FIELDS = 'DateTime DeletedDT ENewsLocation HasPhoto IsVideoLive LastChangeDT LastChangeUser LastChangeUsername No PhotoUrl PublishOnBeach PublishOnDevelopment PublishOnFivb PublishOnHeadlines PublishOnHome PublishOnMedical PublishOnMsdp PublishOnPresident PublishOnRefereeingRules PublishOnSnow PublishOnTechnicalCoach PublishOnTournament PublishOnTwitter PublishOnVolley PublishOnVolleyballWorld PublishOnWorldVolleyNews ShareUrl Source Url ValidFrom ValidTo	DateTime Version VideoUri'

class Article():
    def __init__(self):
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def get(self, no, fields=FIELDS, response_format='xml'):
        url = self.base_url + f"<Request Type='GetArticle' No='{no}' Fields='{fields}'/>"

        if response_format != 'json' and response_format != 'xml':
            raise ValueError(f'{response_format}: The provided value is not accepted.')
        
        headers = {'Accept': f'application/{response_format}'}

        response = requests.get(url, headers=headers)

        if response_format == 'xml':
            return response.text
        elif response_format == 'json':
            return response.json()

    def list(self, fields=FIELDS, filters='', tags='', response_format='xml'):
        url = self.base_url + f"<Request Type='GetArticleList' Fields='{fields}'><Filter>'{filters}'<Tags>{tags}</Tags></Filter></Request>"

        if response_format != 'json' and response_format != 'xml':
            raise ValueError(f'{response_format}: The provided value is not accepted.')

        headers = {'Accept': f'application/{response_format}'}

        response = requests.get(url, headers=headers)

        if response_format == 'xml':
            return response.text
        elif response_format == 'json':
            return response.json()