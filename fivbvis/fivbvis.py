import httpx

class FivbVis():
    def __init__(self):
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def make_request(self, url, request_type, content_type):
        if content_type != 'json' and content_type != 'xml':
            raise ValueError(f'{content_type}: The provided value is not accepted.')

        headers = {'Accept': f'application/{content_type}'}
        response = httpx.get(url, headers=headers)

        if content_type == 'xml':
            return response.text
        elif content_type == 'json':
            return response.json()

    def get(self, request_type, no, fields, content_type):
        url = self.base_url + f"<Request Type='{request_type}' No='{no}' Fields='{fields}'/>"
        return self.make_request(url, request_type, content_type)

    def get_list(self, request_type, no_tournament, fields, filter, content_type):
        url = self.base_url + f"<Request Type='{request_type}' Fields='{fields}'><Filter {filter} NoTournament='{no_tournament}' /></Request>"
        return self.make_request(url, request_type, content_type)

    def get_list_with_tags(self, request_type, fields, filter, tags, content_type):
        url = self.base_url + f"<Request Type='{request_type}' Fields='{fields}'><Filter>'{filter}'<Tags>{tags}</Tags></Filter></Request>"
        return self.make_request(url, request_type, content_type)

    def get_list_without_no(self, request_type, fields, filter, content_type):
        url = self.base_url + f"<Request Type='{request_type}' Fields='{fields}'><Filter {filter} /></Request>"
        return self.make_request(url, request_type, content_type)