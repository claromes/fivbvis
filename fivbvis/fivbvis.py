import httpx
import json
import urllib

class FivbVis():
    def __init__(self):
        self.base_url = 'https://www.fivb.org/Vis2009/XmlRequest.asmx?Request='

    def make_request(self, url, request_type, content_type):
        accepted_content_types = ['json', 'xml']

        if content_type not in accepted_content_types:
            raise ValueError(f'{content_type}: The provided value is not accepted.')

        headers = {'Accept': f'application/{content_type}'}
        response = httpx.get(url, headers=headers, timeout=20.0)

        if content_type == 'xml':
            return response.text
        elif content_type == 'json':
            return json.dumps(response.json(), ensure_ascii=False)

    def set_fields(self, fields):
        if fields:
            return f'Fields="{fields}"'

        return ''

    def set_filter(self, filter):
        if filter:
            return f'<Filter {filter}/>'

        return ''

    def set_tags(self, tags):
        if tags:
            tags = urllib.parse.quote(tags)
            return f'<Filter><Tags>{tags}</Tags></Filter>'

        return ''

    def get(self, request_type, no, fields, content_type='xml'):
        fields = self.set_fields(fields)

        url = self.base_url + f'<Request Type="{request_type}" No="{no}" {fields}/>'
        return self.make_request(url, request_type, content_type)

    def get_list(self, request_type, fields, filter, content_type='xml'):
        fields = self.set_fields(fields)
        filter = self.set_filter(filter)

        url = self.base_url + f'<Request Type="{request_type}" {fields}> {filter}</Request>'
        return self.make_request(url, request_type, content_type)

    def get_list_with_tags(self, request_type, fields, tags, content_type='xml'):
        fields = self.set_fields(fields)
        tags = self.set_tags(tags)

        url = self.base_url + f'<Request Type="{request_type}" {fields}>{tags}</Request>'
        return self.make_request(url, request_type, content_type)
