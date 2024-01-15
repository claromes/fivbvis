# FIVB VIS Python Client

[![PyPI](https://img.shields.io/pypi/v/fivbvis)](https://pypi.org/project/fivbvis/)

Python client library for easy integration with [FIVB VIS Web Service](https://www.fivb.org/VisSDK/VisWebService/#Introduction.html) public data, providing XML and JSON responses.

**This client is not affiliated with the Fédération Internationale de Volleyball (FIVB).**

## Requirements

- Python 3.8+

## Installation

```shell
pip install fivbvis
```

## Usage
Basic example:

```python
from fivbvis import VolleyMatch

vm = VolleyMatch()
print(vm.match(9211, response_format="json"))
```
JSON return:

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
      ...
   }
}
```
## Documentation

[Web Service Requests Reference](docs/reference.md)

## Development

$ `git clone git@github.com:claromes/fivbvis.git`

$ `cd fivbvis`

$ `pip install -r requirements.txt`

## Author

[Claromes](https://claromes.ocom)