import vcr

from pytest import fixture
from fivbvis import Article

#Single Article
@fixture
def article_get_keys():
    return {'data': {'no', 'source', 'publishOnHome', 'videoUri', 'isVideoLive'}}

@vcr.use_cassette('tests/vcr_cassettes/article-get-data.yaml')
def test_article_get(article_get_keys):
    #API call to GET a Article data

    article_get_instance = Article()
    response = article_get_instance.get(28639, 'No')

    assert isinstance(response, dict)
    assert response['data']['no'] == 28639, 'The Article Number should be in the response'
    assert set(article_get_keys).issubset(response.keys()), 'All keys should be in the response'