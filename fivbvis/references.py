import requests

from .fivbvis import FivbVis
from .default_fields import *

class Article(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getArticle(self, no, fields=ARTICLE_DEFAULT_FIELDS, response_format='xml'):
        result = self.fivb_vis.get_with_fields('GetArticle', no, fields, response_format)
        return result

    def getArticleList(self, fields=ARTICLE_DEFAULT_FIELDS, filters='', tags='', response_format='xml'):
        result = self.fivb_vis.get_list_with_tags('GetArticleList', fields, filters, tags, response_format)
        return result

class VolleyMatch(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getMatch(self, no, response_format='xml'):
        result = self.fivb_vis.get('GetVolleyMatch', no, response_format)
        return result

    def getMatchList(self, no_tournament, fields=VOLLEY_MATCH_LIST_DEFAULT_FIELDS, filters='', response_format='xml'):
        result = self.fivb_vis.get_list('GetVolleyMatchList', no_tournament, fields, filters, response_format)
        return result
