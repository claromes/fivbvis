# FIVB VIS Python Client
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/claromes/fivbvis?include_prereleases)
![GitHub](https://img.shields.io/github/license/claromes/fivbvis)

Python client library to easily integrate with FIVB VIS Web Service public data.

Responses are formatted using JSON.

## Installation

```shell
pip3 install fivbvis
```

## Usage
```python
from fivbvis import VolleyMatch

vb = VolleyMatch()

print(vb.match(9211))
```
```json
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

## Docs

[Objects documentation](docs/DOCS.md)

## Development

$ `git clone git@github.com:claromes/fivbvis.git`

$ `cd fivbvis`

$ `pip3 install -r dev-requirements.txt`

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
