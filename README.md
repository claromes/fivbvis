# FIVB VIS Python Client
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/openvb/fivbvis?include_prereleases)
![GitHub](https://img.shields.io/github/license/openvb/fivbvis)

Python client library to easily integrate with FIVB VIS Web Service public data.

Responses are formatted using JSON.

## Installation

PyPI soon.

## Development

$ `git clone git@github.com:openvb/fivbvis.git`

$ `cd fivbvis`

$ `pip install -r requirements.txt`

## Usage
```python
>>> from fivbvis import VolleyMatch
>>> vm = VolleyMatch()
>>> print(vm.match(9211))
{
   "data":{
        "assistantScorerCountryCode":"None",
        "assistantScorerFirstName":"None",
        "assistantScorerLastName":"None",
        "beginDateTimeUtc":"2018-10-07T04:25:00Z",
        "buyTicketsUrl":"",
        "city":"Nagoya",
        "countryCode":"JP",
        "countryName":"Japan",
        "dateLocal":"2018-10-07",
        ...
   }
}
```

## Documentation (WIP)

### Article Object
----

### Beach Object
----

### Confederation Object
----

### Federation Object
----

### Image Object
----

### Match Object
----

### Phase Object
----

### Player Object
----

### Round Object
----

### Tournament Object
----

### VolleyClub Object
----

### VolleyLive Object
----

### VolleyMatch Object
----

`class` fivbvis.VolleyMatch()

>match(no)

Get a volleyball match.

- Parameters:
    - `no` (int) - The number of the match.

- Example:

    `match(9211)`

- Return type:	dict

>list(no_tournament, fields, filter)

Get a list of volleyball matches.

- Parameters:
    - `no_tournament` (int) - The number of the tournament.
    - `fields` (str) - All the fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)
    - `filter` (str, (optional)) - All the filters in the volleyball match data. Must be space-separated. [(Filter list of each match)](https://www.fivb.org/VisSDK/VisWebService/VolleyMatchFilter.html)

- Example:

    `list(979, 'City Hall MatchPointsA MatchPointsB', 'FirstDate="2017-07-01" LastDate="2017-07-31"')`


- Return type:	dict

### VolleyPlayer Object
----

### VolleyPool Object
----

### VolleyRankingDefinition Object
----

### VolleyStatistic Object
----

### VolleyTeam Object
----

### VolleyTournament Object
----

### VolleyTransfer Object
----
