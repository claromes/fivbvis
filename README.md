# FIVB VIS Python Client

[![PyPI](https://img.shields.io/pypi/v/fivbvis)](https://pypi.org/project/fivbvis/) ![Development Status :: 4 - Beta](https://img.shields.io/badge/development_status-4_--_Beta-yellow) [![PyPI](https://img.shields.io/pypi/dm/fivbvis.svg)](https://pypistats.org/packages/fivbvis)

The package `fivbvis` is a Python client library for easy integration with the [Volleyball Information System Web Service](https://www.fivb.org/VisSDK/VisWebService) of the Fédération Internationale de Volleyball (FIVB), handling public data and only documented requests, and providing XML and JSON responses.

The VIS Web Service enables third party applications to access all public data about volleyball, beach volleyball and other events. This client facilitates access for Python programmers, enabling access to data such as articles, matches, events, images, players, player rankings, and tournaments.

It is compatible with Python versions 3.8 and above, but it has been tested specifically on versions 3.8 and 3.11.

## Installation

```shell
pip install fivbvis
```

## Usage
Basic example:

```python
from fivbvis import Volleyball

v = Volleyball()
v.getVolleyMatch(9211, fields="City CountryName DateLocal TeamNameA TeamNameB")
```
XML response:

```xml
<VolleyballMatch
   City="Nagoya"
   CountryName="Japan"
   DateLocal="2018-10-07"
   TeamNameA="Germany"
   TeamNameB="Brazil"
   No="9211"
   Version="2393792"/>
```

## Documentation

The documentation is based on FIVB VIS Web Service requests. It is simple and includes only requests documented by the FIVB developer team. Check the [docs folder](https://github.com/claromes/fivbvis/blob/main/docs/documentation.md) for detailed information and examples.

[This list contains all available requests via VIS web service](https://www.fivb.org/VisSDK/VisWebService/#RequestList.html); those with links are documented. Currently, this Python client is read-only.


## Author

[Claromes](https://claromes.com)