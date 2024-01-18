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

`class` Beach()

> ### getBeachMatch(no, fields response_format)

Get a beach volleyball match.

- Parameters:
    - `no` (int, mandatory) - The number of the match.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

        If the `fields` parameter is not passed, the following fields will be applied: `NoInTournament LocalDate LocalTime TeamAType TeamAName TeamBType TeamBName Court MatchPointsA MatchPointsB`.

    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import Beach

    beach = Beach()
    print(beach.getBeachMatch(15592))
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
    from fivbvis import Beach

    beach = Beach()
    print(beach.getBeachMatchList(filter='NoTournament="502"'))

<br>

> ### getBeachOlympicSelectionRanking()

Get the beach volleyball selection ranking for the Olympic Games.

Only XML response.

<br>

> ### getBeachRound()

Get a beach volleyball round.

Only XML response.

<br>

> ### getBeachRoundList()

Get a list of beach volleyball rounds.

Only XML response.

<br>

> ### getBeachRoundRanking()

Get the ranking of a beach volleyball round.

Only XML response.

<br>

> ### getBeachTeam()

Get a beach volleyball team.

<br>

> ### getBeachTeamList()

Get a list of beach volleyball teams.

<br>

> ### getBeachTournament()

Get a beach volleyball tournament.

<br>

> ### getBeachTournamentRanking()

Get the ranking of a beach volleyball tournament.

Only XML response.

<br>

> ### getBeachWorldTourRanking()

Get a beach volleyball World Tour ranking.

Only XML response.

<br>

## Event `WIP`

`class` Event()

> ### getEvent()

Get an event.

Only XML response.

<br>

> ### getEventList()

Get a list of events.

Only XML response.

<br>

## Image `WIP`

`class` Image()

> ### getImage()	

Get the content of an image.

<br>

## Player `WIP`

`class` Player()

> ### getPlayer()

Get a player.

<br>

## Volleyball `WIP`

`class` Volleyball()

> ### getVolleyMatch(no, response_format)

Get a volleyball match.

- Parameters:
    - `no` (int, mandatory) - The number of the match.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

        If the `fields` parameter is not passed, the following fields will be applied: `City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName`.

    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import Volleyball

    volley = Volleyball()
    print(volley.GetVolleyMatch(9211))
    ```

<br>

> ### getVolleyMatchList(no_tournament, fields, filter, response_format)

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
    from fivbvis import Volleyball

    volley = Volleyball()
    print(volley.getVolleyMatchList(no_tournament=979, filter='FirstDate="2017-7-5" LastDate="2017-7-5"'))
    ```

<br>

> ### getVolleyPlayer()

Get a registration of a player in a volleyball tournament.

<br>

> ### getVolleyPlayerList()

Get a list of registrations of players in volleyball tournaments.

<br>

> ### getVolleyPlayersRankingList()

Get the list of rankings of players in a volleyball tournament.

Only XML response.

<br>

> ### getVolleyPool()

Get a volleyball pool.

<br>

> ### getVolleyPoolList()

Get a list of volleyball pools.

<br>

> ### getVolleyPoolRanking()

Get the ranking for a volleyball pool.

<br>

> ### getVolleyTeam()

Get a registration of a team in a volleyball tournament.

<br>

> ### getVolleyTeamList()

Get a list of registrations of teams in volleyball tournaments.

<br>

> ### getVolleyTournament()

Get a volleyball tournament.

<br>

> ### getVolleyTournamentList()

Get a list of volleyball tournaments.

<br>

> ### getVolleyTournamentRanking()

Get the ranking of a volleyball tournament.
Note: the `teamType` property is not available in JSON.
