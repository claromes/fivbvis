# FIVB VIS Python Client

[![PyPI](https://img.shields.io/pypi/v/fivbvis)](https://pypi.org/project/fivbvis/)

Python client library to easily integrate with [FIVB VIS Web Service](https://www.fivb.org/VisSDK/VisWebService/#Introduction.html) public data.

Responses are formatted using JSON.

## Installation

```shell
pip3 install fivbvis
```

## Usage
```python
from fivbvis import VolleyMatch

vm = VolleyMatch()

print(vm.match(9211))
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
      "dateTimeLocal":"2018-10-07T13:25:00",
      "dateTimeUtc":"2018-10-07T04:25:00Z",
      "durationSet1":1320,
      "durationSet2":1560,
      "durationSet3":2520,
      "durationSet4":1680,
      "durationSet5":1080,
      "durationSet6":"None",
      "durationSet7":"None",
      "durationTotal":8160,
      "endDateTimeUtc":"2018-10-07T06:53:00Z",
      "endTime":"15:53:00",
      "format":1,
      "fullDuration":8880,
      "hall":"Nippongaishi Hall",
      "hasLiveData":1,
      "isFreeEntrance":0,
      "isVtsAvailable":0,
      "lineJudge1CountryCode":"None",
      "lineJudge1FirstName":"None",
      "lineJudge1LastName":"None",
      "lineJudge2CountryCode":"None",
      "lineJudge2FirstName":"None",
      "lineJudge2LastName":"None",
      "lineJudge3CountryCode":"None",
      "lineJudge3FirstName":"None",
      "lineJudge3LastName":"None",
      "lineJudge4CountryCode":"None",
      "lineJudge4FirstName":"",
      "lineJudge4LastName":"None",
      "liveScoreFromScoresheet":1,
      "liveStreamUri":"https://welcome.volleyballworld.tv/",
      "loserRank":0,
      "matchPointsA":3,
      "matchPointsB":2,
      "matchResultText":"3-2",
      "nbSets":5,
      "nbSpectators":3000,
      "no":9211,
      "noConfederation":"None",
      "noDocumentP2":256122695,
      "noEvent":658,
      "noInTournament":63,
      "noPool":2421,
      "noPoolRound":130,
      "noReferee1":150966,
      "noReferee2":153275,
      "noReferee3":"None",
      "noRefereeChallenge":150773,
      "noRefereeReserve":151023,
      "noTeamA":3675,
      "noTeamB":3694,
      "noTournament":1029,
      "pointsTeamASet1":14,
      "pointsTeamASet2":19,
      "pointsTeamASet3":32,
      "pointsTeamASet4":25,
      "pointsTeamASet5":17,
      "pointsTeamASet6":"None",
      "pointsTeamASet7":"None",
      "pointsTeamBSet1":25,
      "pointsTeamBSet2":25,
      "pointsTeamBSet3":30,
      "pointsTeamBSet4":19,
      "pointsTeamBSet5":15,
      "pointsTeamBSet6":"None",
      "pointsTeamBSet7":"None",
      "poolCode":"E",
      "poolName":"Pool E",
      "poolOrder":5,
      "poolRoundCode":"II",
      "poolRoundName":"Second round",
      "referee1FederationCode":"KOR",
      "referee1Name":"Kang Joo-Hee",
      "referee2FederationCode":"ITA",
      "referee2Name":"Rapisarda Daniele",
      "resultType":0,
      "resultTypeText":"None",
      "scheduleInfo":4,
      "scorerCountryCode":"None",
      "scorerFirstName":"None",
      "scorerLastName":"None",
      "season":"2018",
      "setsResultsText":"(14-25, 19-25, 32-30, 25-19, 17-15)",
      "status":25,
      "statusText":"Result is official",
      "teamACalculatedCode":"GER",
      "teamACalculatedName":"Germany",
      "teamACode":"GER",
      "teamALiberoUniformColor":"Red",
      "teamAName":"Germany",
      "teamAShirtColor":"Black",
      "teamAText":"GER",
      "teamBCalculatedCode":"BRA",
      "teamBCalculatedName":"Brazil",
      "teamBCode":"BRA",
      "teamBLiberoUniformColor":"Blue",
      "teamBName":"Brazil",
      "teamBShirtColor":"Yellow",
      "teamBText":"BRA",
      "teamCodeA":"GER",
      "teamCodeB":"BRA",
      "teamNameA":"Germany",
      "teamNameB":"Brazil",
      "timeLocal":"13:25:00",
      "tournamentCode":"WWCH2018",
      "winnerRank":0
   }
}
```

## [Documentation](https://claromes.github.io/fivbvis)

## Requests Available

- Article
- VolleyMatch

## Development

$ `git clone git@github.com:claromes/fivbvis.git`

$ `cd fivbvis`

$ `pip3 install -r dev-requirements.txt`
