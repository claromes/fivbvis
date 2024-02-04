# FIVB VIS Python Client Documentation

## Article

`class` Article()

- ### `getArticle(no, fields, content_type="xml")`

    Get an article

    #### Parameters

    | name           | type     | data type | description                | note                    |
    |----------------|----------|-----------|----------------------------|-------------------------|
    | `no`           | required | int       | Number of the article      |                         |
    | `fields`       | optional | str       | Fields in the article data | Must be space-separated. If it not specified, all the fields you have access to will be sent. |
    | `content_type` | optional | str       | Response content-type      | `xml` or `json`         |

    #### Resource

    [List of Article Fields](https://www.fivb.org/VisSDK/VisWebService/Article.html)

    #### Example

    ```python
    from fivbvis import Article

    a = Article()
    a.getArticle(no=69213, fields="no source isVideoLive", content_type="json")
    ```

- ### `getArticleListWithFilter(fields, filter, content_type="xml")`

    Get a list of article filtering with `PressReleasePublishOn` type

    #### Parameters

    | name           | type     | data type | description                       | note                    |
    |----------------|----------|-----------|-----------------------------------|-------------------------|
    | `fields`       | required | str       | Fields in the article data        | Must be space-separated |
    | `filter`       | optional | str       | Where the articles were published | Must be space-separated. If it is not specified, the response will contain all the articles. |
    | `content_type` | optional | str       | Response content-type             | `xml` or `json`         |

    #### Resources

    [List of Article Fields](https://www.fivb.org/VisSDK/VisWebService/Article.html)

    [List of Article Filter](https://www.fivb.org/VisSDK/VisWebService/ArticleFilter.html)

    #### Example

    ```python
    from fivbvis import Article

    a = Article()
    a.getArticleListWithFilter(fields="no Source", filter="PublishOn='Medical'")
    ```

- ### `getArticleListWithTags(fields, tags, content_type="xml")`

    Get a list of article filtering with `tags`

    #### Parameters

    | name           | type     | data type | description                       | note                    |
    |----------------|----------|-----------|-----------------------------------|-------------------------|
    | `fields`       | required | str       | Fields in the article data        | Must be space-separated |
    | `tags`         | optional | str       | Tags in the article data          | Must be space-separated. If it not specified, all the fields you have access to will be sent.  |
    | `content_type` | optional | str       | Response content-type             | `xml` or `json`         |

    #### Resources

    [List of Article Fields](https://www.fivb.org/VisSDK/VisWebService/Article.html)

    [Tags Filtering](https://www.fivb.org/VisSDK/VisWebService/TagFiltering.html)

    #### Example

    ```python
    from fivbvis import Article

    a = Article()
    a.getArticleListWithTags(fields="no Source", tags="#player-profile volley-tournament:979")
    ```

## Beach `WIP`

`class` Beach()

- ### `getBeachMatch(no, fields, content_type="xml")`

    Get a beach volleyball match

    #### Parameters

    | name           | type     | data type | description                               | note                    |
    |----------------|----------|-----------|-------------------------------------------|-------------------------|
    | `no`           | required | int       | Number of the match                       |                         |
    | `fields`       | optional | str       | Fields in the beach volleyball match data | Must be space-separated. If it not specified, all the fields you have access to will be sent. |
    | `content_type` | optional | str       | Response content-type                     | `xml` or `json`         |

    #### Resource

    [List of Beach Match Fields](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

    #### Example

    ```python
    from fivbvis import Beach

    b = Beach()
    b.getBeachMatch(15592)
    ```

- ### `getBeachMatchList(fields, filter, content_type="xml")`

    Get a list of beach volleyball matches

    #### Parameters

    | name            | type     | data type | description                                | note                    |
    |-----------------|----------|-----------|--------------------------------------------|-------------------------|
    | `fields`        | required | str       | Fields in the beach volleyball match data  | Must be space-separated |
    | `filter`        | optional | str       | Filters in the beach volleyball match data | Must be space-separated. If it is not specified, the response will contain all the beach volleyball matches. |
    | `content_type`  | optional | str       | Response content-type                      | `xml` or `json`         |

    #### Resources

    [List of Beach Match Fields](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

    [List of Beach Match Filter](https://www.fivb.org/VisSDK/VisWebService/BeachMatchFilter.html)

    #### Example

    ```python
    from fivbvis import Beach

    b = Beach()
    b.getBeachMatchList(filter="NoTournament='502'")
    ```

- ### `getBeachOlympicSelectionRanking()`

    Get the beach volleyball selection ranking for the Olympic Games

    Only XML response

- ### `getBeachRound()`

    Get a beach volleyball round

    Only XML response

- ### `getBeachRoundList()`

    Get a list of beach volleyball rounds

    Only XML response

- ### `getBeachRoundRanking()`

    Get the ranking of a beach volleyball round

    Only XML response

- ### `getBeachTeam()`

    Get a beach volleyball team

- ### `getBeachTeamList()`

    Get a list of beach volleyball teams

- ### `getBeachTournament()`

    Get a beach volleyball tournament

- ### `getBeachTournamentRanking()`

    Get the ranking of a beach volleyball tournament

    Only XML response

- ### `getBeachWorldTourRanking()`

    Get a beach volleyball World Tour ranking

    Only XML response

## Event `WIP`

`class` Event()

- ### `getEvent()`

    Get an event

    Only XML response

- ### `getEventList()`

    Get a list of events

    Only XML response

## Image `WIP`

`class` Image()

- ### `getImage()`

    Get the content of an image

## Player `WIP`

`class` Player()

- ### `getPlayer()`

    Get a player

## Volleyball `WIP`

`class` Volleyball()

- ### `getVolleyMatch(no, fields, content_type="xml")`

    Get a volleyball match

    #### Parameters

    | name           | type     | data type | description                         | note                    |
    |----------------|----------|-----------|-------------------------------------|-------------------------|
    | `no`           | required | int       | Number of the match                 |                         |
    | `fields`       | optional | str       | Fields in the volleyball match data | Must be space-separated. If it not specified, all the fields you have access to will be sent. |
    | `content_type` | optional | str       | Response content-type               | `xml` or `json`         |

    #### Resource

    [List of Volley Match Fields](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

    #### Example

    ```python
    from fivbvis import Volleyball

    v = Volleyball()
    v.GetVolleyMatch(9211)
    ```

- ### `getVolleyMatchList(fields, filter, content_type="xml")`

    Get a list of volleyball matches

    #### Parameters

    | name            | type     | data type | description                          | note                    |
    |-----------------|----------|-----------|--------------------------------------|-------------------------|
    | `fields`        | required | str       | Fields in the volleyball match data  | Must be space-separated |
    | `filter`        | optional | str       | Filters in the volleyball match data | Must be space-separated. If it is not specified, the response will contain all the matches. |
    | `content_type`  | optional | str       | Response content-type                | `xml` or `json`         |

    #### Resources

    [List of Volley Match Fields](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

    [List of Volley Match Filter](https://www.fivb.org/VisSDK/VisWebService/VolleyMatchFilter.html)

    #### Example

    ```python
    from fivbvis import Volleyball

    v = Volleyball()
    v.getVolleyMatchList(fields="No NoInTournament DateTimeLocal DateTimeUtc City Hall MatchPointsA MatchPointsB", filter="FirstDate='2017-10-1' LastDate='2017-10-5'")
    ```

- ### `getVolleyPlayer()`

    Get a registration of a player in a volleyball tournament

- ### `getVolleyPlayerList()`

    Get a list of registrations of players in volleyball tournaments

- ### `getVolleyPlayersRankingList()`

    Get the list of rankings of players in a volleyball tournament

    Only XML response

- ### `getVolleyPool()`

    Get a volleyball pool

- ### `getVolleyPoolList()`

    Get a list of volleyball pools

- ### `getVolleyPoolRanking()`

    Get the ranking for a volleyball pool

- ### `getVolleyTeam()`

    Get a registration of a team in a volleyball tournament

- ### `getVolleyTeamList()`

    Get a list of registrations of teams in volleyball tournaments

- ### `getVolleyTournament()`

    Get a volleyball tournament

- ### `getVolleyTournamentList()`

    Get a list of volleyball tournaments

- ### `getVolleyTournamentRanking()`

    Get the ranking of a volleyball tournament

    Note: the `teamType` property is not available in JSON
