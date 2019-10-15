# Weather Observed

## Public instance

You can read about public instance offering information about observed weather
[here](https://github.com/FIWARE/data-models/blob/master/specs/gsma.md).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?type=WeatherObserved&options=keyValues&q=address.addressLocality:Barcelona' \
  -H 'fiware-service: weather' \
  -H 'fiware-servicepath: /Spain' | python -m json.tool
```

```json
[
    {
        "address": {
            "addressCountry": "ES",
            "addressLocality": "Barcelona"
        },
        "dataProvider": "FIWARE",
        "dateObserved": "2019-05-27T21:00:00.00Z",
        "id": "Spain-WeatherObserved-0201D-latest",
        "location": {
            "coordinates": [2.2, 41.3906],
            "type": "Point"
        },
        "precipitation": 0,
        "relativeHumidity": 90,
        "source": "http://www.aemet.es",
        "stationCode": "0201D",
        "stationName": "Barcelona",
        "temperature": 17,
        "type": "WeatherObserved",
        "windDirection": 105,
        "windSpeed": 3.5
    }
]
```
