import requests

class FivbVis():
    def __init__(self):
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def make_request(self, url, request_type, response_format):
        if response_format != 'json' and response_format != 'xml':
            raise ValueError(f'{response_format}: The provided value is not accepted.')

        headers = {'Accept': f'application/{response_format}'}
        response = requests.get(url, headers=headers)

        if response_format == 'xml':
            return response.text
        elif response_format == 'json':
            return response.json()

    def get(self, request_type, no, response_format):
        url = self.base_url + f"<Request Type='{request_type}' No='{no}' />"
        return self.make_request(url, request_type, response_format)

    def get_with_fields(self, request_type, no, fields, response_format):
        url = self.base_url + f"<Request Type='{request_type}' No='{no}' Fields='{fields}'/>"
        return self.make_request(url, request_type, response_format)

    def get_list(self, request_type, no_tournament, fields, filters, response_format):
        url = self.base_url + f"<Request Type='{request_type}' Fields='{fields}'><Filter {filters} NoTournament='{no_tournament}' /></Request>"
        return self.make_request(url, request_type, response_format)

    def get_list_with_tags(self, request_type, fields, filters, tags, response_format):
        url = self.base_url + f"<Request Type='{request_type}' Fields='{fields}'><Filter>'{filters}'<Tags>{tags}</Tags></Filter></Request>"
        return self.make_request(url, request_type, response_format)