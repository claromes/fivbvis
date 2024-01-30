# FIVB VIS Python Client

[![PyPI](https://img.shields.io/pypi/v/fivbvis)](https://pypi.org/project/fivbvis/) [![VIS Web Service](https://img.shields.io/badge/VIS%20Web%20Service-v24-%234285f4)](https://www.fivb.org/VisSDK/VisWebService/#Introduction.html)


Python client library for easy integration with International Volleyball Federation VIS Web Service, handling public data and only documented requests, and providing XML and JSON responses.

The VIS Web Service enables third party applications to access all public data about volleyball, beach volleyball and other events. FIVB VIS Python Client facilitates access for Python programmers, enabling access to public data such as articles, matches, events, images, players, player rankings, and tournaments.

**This client is not affiliated with the Fédération Internationale de Volleyball (FIVB).**

## Requirement

- Python 3.8+

## Installation

```shell
pip install fivbvis
```

## Usage
Basic example:

```python
from fivbvis import Volleyball

v = Volleyball()
print(v.getVolleyMatch(9211, response_format="json"))
```
JSON return:

```json
{
   "data":{
      "city":"Nagoya",
      "countryName":"Japan",
      "dateTimeLocal":"2018-10-07T13:25:00",
      "durationTotal":8160,
      "hall":"Nippongaishi Hall",
      "matchPointsA":3,
      "matchPointsB":2,
      "matchResultText":"3-2",
      "no":9211,
      "noTournament":1029,
      "season":"2018",
      "teamAName":"Germany",
      "teamBName":"Brazil"
   }
}
```

## Documentation

[Web Service Requests Reference](https://github.com/claromes/fivbvis/blob/main/docs/reference.md)

## Development

$ `git clone git@github.com:claromes/fivbvis.git`

$ `cd fivbvis`

$ `pip install -r requirements.txt`

$ `pip install --editable .`

## Author

[Claromes](https://claromes.com)