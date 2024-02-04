from .fivbvis import FivbVis

class Article(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getArticle(self, no, fields=None, content_type='xml'):
        result = self.fivb_vis.get('GetArticle', no, fields, content_type)
        return result

    def getArticleList(self, fields=None, filter=None, tags=None, content_type='xml'):
        result = self.fivb_vis.get_list_with_tags('GetArticleList', fields, filter, tags, content_type)
        return result

class Beach(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getBeachMatch(self, no, fields=None, content_type='xml'):
        result = self.fivb_vis.get('GetBeachMatch', no, fields, content_type)
        return result

    def getBeachMatchList(self, fields, filter=None, content_type='xml'):
        result = self.fivb_vis.get_list_without_no('GetBeachMatchList', fields, filter, content_type)
        return result

    def getBeachOlympicSelectionRanking():
        return

    def getBeachRound():
        return

    def getBeachRoundList():
        return

    def getBeachRoundRanking():
        return

    def getBeachTeam():
        return

    def getBeachTeamList():
        return

    def getBeachTournament():
        return

    def getBeachTournamentRanking():
        return

    def getBeachWorldTourRanking():
        return
        
class Volleyball(FivbVis):
    def __init__(self):
        self.fivb_vis = FivbVis()

    def getVolleyMatch(self, no, fields=None, content_type='xml'):
        result = self.fivb_vis.get('GetVolleyMatch', no, fields, content_type)
        return result

    def getVolleyMatchList(self, fields=None, filter=None, content_type='xml'):
        result = self.fivb_vis.get_list('GetVolleyMatchList', fields, filter, content_type)
        return result
