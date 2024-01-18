# Web Service Requests Reference

## Article

`class` Article()

> ### getArticle(no, fields, response_format)

Get an article.

- Parameters:
    - `no` (int, mandatory) - The number of the article.
    - `fields` (str, optional) - Fields in the article data. Must be space-separated. [(Fields/Properties list of each article)](https://www.fivb.org/VisSDK/VisWebService/Article.html)

        If the `fields` parameter is not passed, the following fields will be applied: `No Category Source SourceCategory TeamCode TournamentCode NoMatch PublishOnHome VideoUri IsVideoLive`.

    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import Article

    a = Article()
    print(a.getArticle(no=69213, fields="no source isVideoLive"))
    ```

<br>

> ### getArticleList(fields, filter, tags, response_format)

Get a list of article.

- Parameters:
    - `fields` (str, mandatory) - Fields in the article data. Must be space-separated. [(Fields/Properties list of each article)](https://www.fivb.org/VisSDK/VisWebService/Article.html)

        If the `fields` parameter is not passed, the following fields will be applied: `No Category Source SourceCategory TeamCode TournamentCode NoMatch PublishOnHome VideoUri IsVideoLive`.

    - `filter` (str, optional) - Where the articles were published. Must be space-separated. [(Filter for an article)](https://www.fivb.org/VisSDK/VisWebService/ArticleFilter.html)
    - `tags` (str, optional) - Tags in the article data. Must be space-separated. [(Tags Filtering examples)](https://www.fivb.org/VisSDK/VisWebService/TagFiltering.html)
    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import Article

    a = Article()
    print(a.getArticleList(filter="Home", tags="volley-tournament:979"))
    ```

<br>

## Beach

`class` BeachMatch()

> ### (no, fields response_format)

Get a beach volleyball match.

- Parameters:
    - `no` (int, mandatory) - The number of the match.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

        If the `fields` parameter is not passed, the following fields will be applied: `NoInTournament LocalDate LocalTime TeamAType TeamAName TeamBType TeamBName Court MatchPointsA MatchPointsB`.

    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import BeachMatch

    bm = BeachMatch()
    print(bm.getBeachMatch(15592))
    ```

<br>

> ### getBeachMatchList(fields, filter, response_format)

Get a list of beach volleyball matches.

Requesting all parameters may result in a 404 error.

- Parameters:
    - `no_tournament` (int, mandatory) - The number of the tournament.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

        If the `fields` parameter is not passed, the following fields will be applied: `NoInTournament LocalDate LocalTime TeamAName TeamBName Court MatchPointsA MatchPointsB`.

    - `filter` (str, optional) - Filters in the volleyball match data. Must be space-separated. [(Filter list of each match)](https://www.fivb.org/VisSDK/VisWebService/BeachMatchFilter.html)
    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

     ```python
    from fivbvis import BeachMatch

    bm = BeachMatch()
    print(bm.getBeachMatchList(filter='NoTournament="502"'))
    ```

<br>

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

`class` VolleyMatch()

> ### getMatch(no, response_format)

Get a volleyball match.

- Parameters:
    - `no` (int, mandatory) - The number of the match.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

        If the `fields` parameter is not passed, the following fields will be applied: `City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName`.

    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import VolleyMatch

    vm = VolleyMatch()
    print(vm.getMatch(9211))
    ```

<br>

> ### getMatchList(no_tournament, fields, filter, response_format)

Get a list of volleyball matches.

Requesting all parameters may result in a 404 error.

- Parameters:
    - `no_tournament` (int, mandatory) - The number of the tournament.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

        If the `fields` parameter is not passed, the following fields will be applied: `City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName`.

    - `filter` (str, optional) - Filters in the volleyball match data. Must be space-separated. [(Filter list of each match)](https://www.fivb.org/VisSDK/VisWebService/VolleyMatchFilter.html)
    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

     ```python
    from fivbvis import VolleyMatch

    vm = VolleyMatch()
    print(vm.getMatchList(no_tournament=979, filter='FirstDate="2017-7-5" LastDate="2017-7-5"'))
    ```

<br>

## VolleyPlayer

## VolleyPool

## VolleyRankingDefinition

## VolleyStatistic

## VolleyTeam

## VolleyTournament

## VolleyTransfer
