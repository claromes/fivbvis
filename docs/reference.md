# Web Service Requests Reference

## Article

`class` Article()

> ### getArticle(no, fields, response_format)

Get an article.

- Parameters:
    - `no` (int, required) - The number of the article.
    - `fields` (str, optional) - Fields in the article data. Must be space-separated. [(Fields/Properties list of each article)](https://www.fivb.org/VisSDK/VisWebService/Article.html)

        If the `fields` parameter is not passed, the following fields will be applied: `DateTime DeletedDT ENewsLocation HasPhoto IsVideoLive LastChangeDT LastChangeUser LastChangeUsername No PhotoUrl PublishOnBeach PublishOnDevelopment PublishOnFivb PublishOnHeadlines PublishOnHome PublishOnMedical PublishOnMsdp PublishOnPresident PublishOnRefereeingRules PublishOnSnow PublishOnTechnicalCoach PublishOnTournament PublishOnTwitter PublishOnVolley PublishOnVolleyballWorld PublishOnWorldVolleyNews ShareUrl Source Url ValidFrom ValidTo DateTime Version VideoUri`.

    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import Article

    a = Article()
    print(a.getArticle(no=69213, fields="no source isVideoLive"))
    ```

<br>

> ### getArticleList(fields, filters, tags, response_format)

Get a list of article.

- Parameters:
    - `fields` (str, required) - Fields in the article data. Must be space-separated. [(Fields/Properties list of each article)](https://www.fivb.org/VisSDK/VisWebService/Article.html)

        If the `fields` parameter is not passed, the following fields will be applied: `DateTime DeletedDT ENewsLocation HasPhoto IsVideoLive LastChangeDT LastChangeUser LastChangeUsername No PhotoUrl PublishOnBeach PublishOnDevelopment PublishOnFivb PublishOnHeadlines PublishOnHome PublishOnMedical PublishOnMsdp PublishOnPresident PublishOnRefereeingRules PublishOnSnow PublishOnTechnicalCoach PublishOnTournament PublishOnTwitter PublishOnVolley PublishOnVolleyballWorld PublishOnWorldVolleyNews ShareUrl Source Url ValidFrom ValidTo DateTime Version VideoUri`.

    - `filters` (str, optional) - Where the articles were published. Must be space-separated. [(Filter for an article)](https://www.fivb.org/VisSDK/VisWebService/ArticleFilter.html)
    - `tags` (str, optional) - Tags in the article data. Must be space-separated. [(Tags Filtering examples)](https://www.fivb.org/VisSDK/VisWebService/TagFiltering.html)
    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import Article

    a = Article()
    print(a.getArticleList(filters="Home", tags="volley-tournament:979"))
    ```

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

`class` VolleyMatch()

> ### getMatch(no, response_format)

Get a volleyball match.

- Parameters:
    - `no` (int, required) - The number of the match.
    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

    ```python
    from fivbvis import VolleyMatch

    vm = VolleyMatch()
    print(vm.getMatch(9211))
    ```

<br>

> ### getMatchList(no_tournament, fields, filters, response_format)

Get a list of volleyball matches.

If the `fields` parameter is not passed, the following fields will be applied: `city countryName dateTimeLocal durationTotal hall matchPointsA matchPointsB matchResultText no noTournament season teamAName teamBName`.

Requesting all parameters may result in a 404 error.

- Parameters:
    - `no_tournament` (int, required) - The number of the tournament.
    - `fields` (str, optional) - Fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)
    - `filters` (str, optional) - Filters in the volleyball match data. Must be space-separated. [(Filter list of each match)](https://www.fivb.org/VisSDK/VisWebService/VolleyMatchFilter.html)
    - `response_format` (str, optional) - The response format: "xml" or "json". By default the response format is XML.

- Example:

     ```python
    from fivbvis import VolleyMatch

    vm = VolleyMatch()
    print(vm.getMatchList(no_tournament=979, filters='FirstDate="2017-7-5" LastDate="2017-7-5"'))
    ```

<br>

## VolleyPlayer

## VolleyPool

## VolleyRankingDefinition

## VolleyStatistic

## VolleyTeam

## VolleyTournament

## VolleyTransfer
