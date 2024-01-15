# Web Service Requests Reference

## Article

>`class` fivbvis.Article()

### get(no, fields=None)

Get an article.

- Parameters:
    - `no` (int, required) - The number of the match.
    - `fields` (str, optional) - All the fields in the article data. Must be space-separated. [(Fields/Properties list of each article)](https://www.fivb.org/VisSDK/VisWebService/Article.html)

- Example:

    ```python
    from fivbvis import Article

    a = Article()
    print(a.get(69213, 'no source isVideoLive'))
    ```

- Return type: `dict`

### list(fields, filter=None, tags=None)

Get a list of article.

- Parameters:
    - `fields` (str, required) - All the fields in the article data. Must be space-separated. [(Fields/Properties list of each article)](https://www.fivb.org/VisSDK/VisWebService/Article.html)
    - `filter` (str, optional) - Where the articles were published. Must be space-separated. [(Filter for an article)](https://www.fivb.org/VisSDK/VisWebService/ArticleFilter.html)
    - `tags` (str, optional) - Tags in the article data. Must be space-separated. [(Tags Filtering examples)](https://www.fivb.org/VisSDK/VisWebService/TagFiltering.html)

- Example:

    ```python
    from fivbvis import Article

    a = Article()
    print(a.list('no photoUrl publishOnFivb shareUrl', 'home', 'volley-tournament:979'))
    ```

- Return type: `dict`

<br>

## Beach

## Confederation

## Federation

## Image

## Match

## Phase

## Player

## Round

## Tournament

## VolleyClub

## VolleyLive

## VolleyMatch

>`class` fivbvis.VolleyMatch()

### match(no)

Get a volleyball match.

- Parameters:
    - `no` (int, required) - The number of the match.

- Example:

    ```python
    from fivbvis import VolleyMatch

    vm = VolleyMatch()
    print(vm.match(9211))
    ```

- Return type: `dict`

### list(no_tournament, fields=None, filter=None)

Get a list of volleyball matches.

- Parameters:
    - `no_tournament` (int, required) - The number of the tournament.
    - `fields` (str, optional) - All the fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)
    - `filter` (str, optional) - All the filters in the volleyball match data. Must be space-separated. [(Filter list of each match)](https://www.fivb.org/VisSDK/VisWebService/VolleyMatchFilter.html)

- Example:

     ```python
    from fivbvis import VolleyMatch

    vm = VolleyMatch()
    print(vm.list(979, 'city hall matchPointsA matchPointsB', 'firstDate="2017-07-01" lastDate="2017-07-31"'))
    ```

- Return type: `dict`

<br>

## VolleyPlayer

## VolleyPool

## VolleyRankingDefinition

## VolleyStatistic

## VolleyTeam

## VolleyTournament

## VolleyTransfer
