from fivbvis import Article, BeachMatch, VolleyMatch

a = Article()
bm = BeachMatch()
vm = VolleyMatch()

# print(a.getArticle(69213))
# print(a.getArticle(69213, response_format='json'))

# print(a.getArticleList(fields='no', filter='home', tags='volley-tournament:979'))
# print(a.getArticleList(fields='no', filter='home', tags='volley-tournament:979', response_format='json'))

# print(vm.getMatch(9211))
print(vm.getMatch(9211, response_format='json'))

# print(vm.getMatchList(979, filter='FirstDate="2017-7-5" LastDate="2017-7-5"'))
# print(vm.getMatchList(979, filter='FirstDate="2017-7-5" LastDate="2017-7-5"', response_format='json'))

# print(bm.getBeachMatch(15592))
# print(bm.getBeachMatch(15592, response_format='json'))

# print(bm.getBeachMatchList(filter='NoTournament="502"'))
# print(bm.getBeachMatchList(filter='NoTournament="502"', response_format='json'))

