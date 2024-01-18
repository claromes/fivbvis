import requests

from .fivbvis import FivbVis
from .default_fields import *

class Article(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getArticle(self, no, fields=ARTICLE_DEFAULT_FIELDS, response_format='xml'):
        result = self.fivb_vis.get('GetArticle', no, fields, response_format)
        return result

    def getArticleList(self, fields=ARTICLE_DEFAULT_FIELDS, filter='', tags='', response_format='xml'):
        result = self.fivb_vis.get_list_with_tags('GetArticleList', fields, filter, tags, response_format)
        return result

class BeachMatch(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getBeachMatch(self, no, fields=BEACH_MATCH_DEFAULT_FIELDS, response_format='xml'):
        result = self.fivb_vis.get('GetBeachMatch', no, fields, response_format)
        return result

    def getBeachMatchList(self, fields=BEACH_MATCH_LIST_DEFAULT_FIELDS, filter='', response_format='xml'):
        result = self.fivb_vis.get_list_without_no('GetBeachMatchList', fields, filter, response_format)
        return result

class VolleyMatch(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getMatch(self, no, fields=VOLLEY_MATCH_DEFAULT_FIELDS, response_format='xml'):
        result = self.fivb_vis.get('GetVolleyMatch', no, fields, response_format)
        return result

    def getMatchList(self, no_tournament, fields=VOLLEY_MATCH_DEFAULT_FIELDS, filter='', response_format='xml'):
        result = self.fivb_vis.get_list('GetVolleyMatchList', no_tournament, fields, filter, response_format)
        return result
