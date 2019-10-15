# Weather Forecast

## Public instance

You can read about public instance offering information about weather forecast
[here](https://github.com/FIWARE/data-models/blob/master/specs/gsma.md).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?id=Spain-WeatherForecast-28079_tomorrow_18:00:00_00:00:00&options=keyValues' \
  -H 'fiware-service: weather'| python -m json.tool
```

```json
[
    {
        "address": {
            "addressCountry": "ES",
            "addressLocality": "Madrid",
            "postalCode": "28079"
        },
        "dataProvider": "FIWARE",
        "dateIssued": "2019-06-13T00:00:00.00Z",
        "dateRetrieved": "2019-06-13T12:42:59.00Z",
        "dayMaximum": {
            "feelsLikeTemperature": 26,
            "relativeHumidity": 0.4,
            "temperature": 26
        },
        "dayMinimum": {
            "feelsLikeTemperature": 14,
            "relativeHumidity": 0.15,
            "temperature": 14
        },
        "feelsLikeTemperature": 16,
        "id": "Spain-WeatherForecast-28079_tomorrow_18:00:00_00:00:00",
        "precipitationProbability": 0,
        "relativeHumidity": 0.4,
        "source": "http://www.aemet.es",
        "temperature": 16,
        "type": "WeatherForecast",
        "validFrom": "2019-06-14T18:00:00.00Z",
        "validTo": "2019-06-15T00:00:00.00Z",
        "validity": "2019-06-14T18:00:00Z/2019-06-15T00:00:00Z",
        "weatherType": "sunnyDay",
        "windDirection": 90,
        "windSpeed": 4.2
    }
]
```
