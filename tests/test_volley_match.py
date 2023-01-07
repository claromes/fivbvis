import vcr

from pytest import fixture
from fivbvis import VolleyMatch

#Single Match
@fixture
def volley_match_keys():
    return {'data': {'no', 'dateTimeLocal', 'city', 'hall', 'teamA', 'teamB', 'tournament'}}

@vcr.use_cassette('tests/vcr_cassettes/volley-match-data.yaml')
def test_volley_match(volley_match_keys):
    #API call to GET a Volleyball match data

    volley_match_instance = VolleyMatch()
    response = volley_match_instance.match(7604)

    assert isinstance(response, dict)
    assert response['data']['no'] == 7604, 'The Match Number should be in the response'
    assert set(volley_match_keys).issubset(response.keys()), 'All keys should be in the response'

#Match List
@fixture
def volley_list_keys():
    return {'data': [{'no', 'teamA', 'teamB', 'noTournament'}, {'no', 'teamA', 'teamB', 'noTournament'}]}

@vcr.use_cassette('tests/vcr_cassettes/volley-list-data.yaml')
def test_volley_list(volley_list_keys):
    #API call to GET a Volleyball list data

    volley_list_instance = VolleyMatch()
    response = volley_list_instance.list(979, "no teamA teamB noTournament", "FirstDate='2017-07-01' LastDate='2017-07-31'")

    assert isinstance(response, dict)

    assert response['data'][0]['noTournament'] == 979, 'The Tournament Number of the first match should be in the response'
    assert response['data'][1]['noTournament'] == 979, 'The Tournament Number of the second match should be in the response'

    assert response['data'][0]['no'] == 7595, 'The first Match Number should be in the response'
    assert response['data'][1]['no'] == 7596, 'The second Match Number should be in the response'

    assert set(volley_list_keys).issubset(response.keys()), 'All keys should be in the response'