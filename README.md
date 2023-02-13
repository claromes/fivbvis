# FIVB VIS Python Client
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/openvb/fivbvis?include_prereleases)
![GitHub](https://img.shields.io/github/license/openvb/fivbvis)

Python client library to easily integrate with FIVB VIS Web Service public data.

Responses are formatted using JSON.

## Installation

PyPI soon.

## Docs

[Objects documentation](docs/DOCS.md)

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
## Development

$ `git clone git@github.com:openvb/fivbvis.git`

$ `cd fivbvis`

$ `pip install -r requirements.txt`

## Requests

- [x] Article Object

- [ ] Beach Object

- [ ] Confederation Object

- [ ] Federation Object

- [ ] Image Object

- [ ] Match Object

- [ ] Phase Object

- [ ] Player Object

- [ ] Round Object

- [ ] Tournament Object

- [ ] VolleyClub Object

- [ ] VolleyLive Object

- [x] VolleyMatch Object

- [ ] VolleyPlayer Object

- [ ] VolleyPool Object

- [ ] VolleyRankingDefinition Object

- [ ] VolleyStatistic Object

- [ ] VolleyTeam Object

- [ ] VolleyTournament Object

- [ ] VolleyTransfer Object

[VIS Web Service Requests full list](https://www.fivb.org/VisSDK/VisWebService/RequestList.html)
