import vcr

from pytest import fixture
from fivbvis import VolleyMatch

@fixture
def volley_match_keys():
    return {'data': {'no', 'dateTimeLocal', 'city', 'hall', 'teamA', 'teamB', 'tournament'}}

@vcr.use_cassette('tests/vcr_cassettes/volley-match-data.yaml')
def test_volley_match(volley_match_keys):
    '''API call to GET a Volleyball match data'''

    volley_match_instance = VolleyMatch(7604)
    response = volley_match_instance.match()

    assert isinstance(response, dict)
    assert response['data']['no'] == 7604, 'The Match Number should be in the response'
    assert set(volley_match_keys).issubset(response.keys()), 'All keys should be in the response'