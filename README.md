# FIVB VIS Python Client
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/openvb/fivbvis?include_prereleases)
![GitHub](https://img.shields.io/github/license/openvb/fivbvis)

Python library to easily integrate with FIVB VIS Web Service public data.

Responses are formatted using JSON.

## Install

$ `git clone git@github.com:openvb/fivbvis.git`

$ `cd fivbvis`

$ `pip install -r requirements.txt`

PyPI soon.

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

- Return type:	dict

>match_list(no_tournament, fields)

Get a list of volleyball matches.

- Parameters:
    - `no_tournament` (int) - The number of the tournament.
    - `fields` (str) - All the fields in the volleyball match data. Must be space-separated. [(Fields/Properties list of each match)](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

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
