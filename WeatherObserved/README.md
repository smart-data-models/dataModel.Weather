# Weather Observed

## Description

An observation of weather conditions at a certain place and time. This data
model has been developed in cooperation with mobile operators and the
[GSMA](https://www.gsma.com/iot/iot-big-data/).

## Data Model

The specification is available in the [spec.md](./doc/spec.md)

A JSON Schema corresponding to this data model can be found
[here](./schema.json).

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",
    "type": "WeatherObserved",
    "dateObserved": {
        "type": "DateTime",
        "value": "2016-11-30T07:00:00.00Z"
    },
    "illuminance": {
        "value": 1000
    },
    "temperature": {
        "value": 3.3
    },
    "precipitation": {
        "value": 0
    },
    "atmosphericPressure": {
        "value": 938.9
    },
    "pressureTendency": {
        "value": 0.5
    },
    "refDevice": {
        "type": "Relationship",
        "value": "device-0A3478"
    },
    "source": {
        "value": "http://www.aemet.es"
    },
    "windSpeed": {
        "value": 2
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [-4.754444444, 41.640833333]
        }
    },
    "stationName": {
        "value": "Valladolid"
    },
    "address": {
        "type": "PostalAddress",
        "value": {
            "addressLocality": "Valladolid",
            "addressCountry": "ES"
        }
    },
    "stationCode": {
        "value": "2422"
    },
    "dataProvider": {
        "value": "TEF"
    },
    "windDirection": {
        "value": -45
    },
    "relativeHumidity": {
        "value": 1
    },
    "streamGauge": {
        "value": 50
    },
    "snowHeight": {
        "value": 20
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "Spain-WeatherObserved-2422-2016-11-30T08:00:00",
    "type": "WeatherObserved",
    "address": {
        "addressLocality": "Valladolid",
        "addressCountry": "ES"
    },
    "atmosphericPressure": 938.9,
    "dataProvider": "TEF",
    "dateObserved": "2016-11-30T07:00:00.00Z",
    "location": {
        "type": "Point",
        "coordinates": [-4.754444444, 41.640833333]
    },
    "precipitation": 0,
    "pressureTendency": 0.5,
    "relativeHumidity": 1,
    "source": "http://www.aemet.es",
    "stationCode": "2422",
    "stationName": "Valladolid",
    "temperature": 3.3,
    "windDirection": -45,
    "windSpeed": 2,
    "illuminance": 1000
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",
    "type": "WeatherObserved",
    "dateObserved": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2016-11-30T07:00:00.00Z"
        }
    },
    "illuminance": {
        "type": "Property",
        "value": 1000
    },
    "temperature": {
        "type": "Property",
        "value": 3.3
    },
    "precipitation": {
        "type": "Property",
        "value": 0
    },
    "atmosphericPressure": {
        "type": "Property",
        "value": 938.9
    },
    "pressureTendency": {
        "type": "Property",
        "value": 0.5
    },
    "refDevice": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:Device:device-0A3478"
    },
    "source": {
        "type": "Property",
        "value": "http://www.aemet.es"
    },
    "windSpeed": {
        "type": "Property",
        "value": 2
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [-4.754444444, 41.640833333]
        }
    },
    "stationName": {
        "type": "Property",
        "value": "Valladolid"
    },
    "address": {
        "type": "Property",
        "value": {
            "addressLocality": "Valladolid",
            "addressCountry": "ES",
            "type": "PostalAddress"
        }
    },
    "stationCode": {
        "type": "Property",
        "value": "2422"
    },
    "dataProvider": {
        "type": "Property",
        "value": "TEF"
    },
    "windDirection": {
        "type": "Property",
        "value": -45
    },
    "relativeHumidity": {
        "type": "Property",
        "value": 1
    },
    "streamGauge": {
        "type": "Property",
        "value": 50
    },
    "snowHeight": {
        "type": "Property",
        "value": 20
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

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
