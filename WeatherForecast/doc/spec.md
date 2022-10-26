<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: WeatherForecast  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherForecast/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **A harmonised description of a Weather Forecast**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: The atmospheric pressure observed measured in Hecto Pascals  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateIssued[string]`: The date and time the forecast was issued by the meteorological bureau in ISO8601 UTC format.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateRetrieved[string]`: The date and time the forecast was retrieved in ISO8601 UTC format.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dayMaximum[object]`: Maximum values for the reported period. Subattributes:- `temperature` : Maximum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Maximum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.-   `relativeHumidity`. Maximum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dayMinimum[object]`: Minimum values forecasted for the reported period.  Minimum values for the reported period. Subattributes:- `temperature` : Minimum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Minimum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Minimum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: A description of this item  - `feelLikesTemperature[number]`: Temperature appreciation of the item  - `gustSpeed[number]`: A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.  - `id[*]`: Unique identifier of the entity  - `illuminance[number]`: (https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `precipitation[number]`: Amount of water rain expected  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPointOfInterest[string]`: Point of interest related to the item  . Model: [http://schema.org/URL](http://schema.org/URL)- `relativeHumidity[number]`: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `temperature[number]`: Temperature of the item  - `type[string]`: NGSI Entity type. It has to be WeatherForecast  - `uVIndexMax[number]`: The maximum UV index for the period, based on the World Health Organization's UV Index measure. Normative references: [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  . Model: [https://schema.org/Number](https://schema.org/Number)- `validFrom[string]`: Validity period start date and time.  . Model: [https://schema.org/Text](https://schema.org/Text)- `validTo[string]`: Validity period end date and time.  . Model: [https://schema.org/Text](https://schema.org/Text)- `validity[string]`: Includes the validity period for this forecast as a ISO8601 time interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `validFrom`, `validTo`.  . Model: [https://schema.org/Text](https://schema.org/Text)- `visibility[*]`: Categories of visibility  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: Text description of the weather  . Model: [http://schema.org/Text.](http://schema.org/Text.)- `windDirection[number]`: Direction of the wind bet  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: Intensity of the wind  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `address`  - `dateIssued`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
This entity is primarily associated with the vertical segments of the environment and agriculture but is applicable to many different applications. This data model has been developed in cooperation with mobile operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherForecast:    
  description: 'A harmonised description of a Weather Forecast'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    atmosphericPressure:    
      description: 'The atmospheric pressure observed measured in Hecto Pascals'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Hecto pascals'    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateIssued:    
      description: 'The date and time the forecast was issued by the meteorological bureau in ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateRetrieved:    
      description: 'The date and time the forecast was retrieved in ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dayMaximum:    
      description: 'Maximum values for the reported period. Subattributes:- `temperature` : Maximum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Maximum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.-   `relativeHumidity`. Maximum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`.'    
      properties:    
        feelLikesTemperature:    
          description: 'Property. Temperature appreciation of the item'    
          type: number    
        relativeHumidity:    
          description: 'Property. Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
          maximum: 1    
          minimum: 0    
          type: number    
        temperature:    
          description: 'Property. Temperature of the item'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dayMinimum:    
      description: 'Minimum values forecasted for the reported period.  Minimum values for the reported period. Subattributes:- `temperature` : Minimum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Minimum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Minimum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`'    
      properties:    
        feelLikesTemperature:    
          description: 'Property. Temperature appreciation of the item'    
          type: number    
        relativeHumidity:    
          description: 'Property. Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
          maximum: 1    
          minimum: 0    
          type: number    
        temperature:    
          description: 'Property. Temperature of the item'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: 'A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &weatherforecast_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *weatherforecast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: 'Amount of water rain expected'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Liters per square meter.'    
    refPointOfInterest:    
      description: 'Point of interest related to the item'    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    relativeHumidity:    
      description: 'Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WeatherForecast'    
      enum:    
        - WeatherForecast    
      type: string    
      x-ngsi:    
        type: Property    
    uVIndexMax:    
      description: 'The maximum UV index for the period, based on the World Health Organization''s UV Index measure. Normative references: [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    validFrom:    
      description: 'Validity period start date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    validTo:    
      description: 'Validity period end date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `validFrom`, `validTo`.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    visibility:    
      anyOf:    
        - enum:    
            - veryPoor    
            - poor    
            - moderate    
            - good    
            - veryGood    
            - excellent    
          type: string    
        - minimum: 0    
          type: number    
      description: 'Categories of visibility'    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    weatherType:    
      description: 'Text description of the weather'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text.    
        type: Property    
    windDirection:    
      description: 'Direction of the wind bet'    
      maximum: 180    
      minimum: -180    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    windSpeed:    
      description: 'Intensity of the wind'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - dateIssued    
    - address    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherForecast/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### WeatherForecast NGSI-v2 key-values Example    
Here is an example of a WeatherForecast in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
  "type": "WeatherForecast",  
  "address": {  
    "addressCountry": "Spain",  
    "postalCode": "46005",  
    "addressLocality": "Valencia"  
  },  
  "dataProvider": "TEF",  
  "dateIssued": "2016-12-01T10:40:01.00Z",  
  "dateRetrieved": "2016-12-01T12:57:24.00Z",  
  "dayMaximum": {  
    "feelsLikeTemperature": 15,  
    "temperature": 15,  
    "relativeHumidity": 0.9  
  },  
  "dayMinimum": {  
    "feelsLikeTemperature": 11,  
    "temperature": 11,  
    "relativeHumidity": 0.7  
  },  
  "feelsLikeTemperature": 12,  
  "precipitationProbability": 0.15,  
  "relativeHumidity": 0.85,  
  "source": "http://www.aemet.es/xml/municipios/localidad_46250.xml",  
  "temperature": 12,  
  "validFrom": "2016-12-01T17:00:00.00Z",  
  "validTo": "2016-12-01T23:00:00.00Z",  
  "validity": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00",  
  "weatherType": "overcast",  
  "windSpeed": 0,  
  "uVIndexMax": 1  
}  
```  
</details>  
#### WeatherForecast NGSI-v2 normalized Example    
Here is an example of a WeatherForecast in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
  "type": "WeatherForecast",  
  "dayMinimum": {  
    "type": "StructuredValue",  
    "value": {  
      "feelsLikeTemperature": 11,  
      "temperature": 11,  
      "relativeHumidity": 0.7  
    }  
  },  
  "feelsLikeTemperature": {  
    "type": "Number",  
    "value": 12  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "TEF"  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 12  
  },  
  "validTo": {  
    "type": "DateTime",  
    "value": "2016-12-01T23:00:00.00Z"  
  },  
  "weatherType": {  
    "type": "Text",  
    "value": "overcast"  
  },  
  "precipitationProbability": {  
    "type": "Number",  
    "value": 0.15  
  },  
  "dayMaximum": {  
    "type": "StructuredValue",  
    "value": {  
      "feelsLikeTemperature": 15,  
      "temperature": 15,  
      "relativeHumidity": 0.9  
    }  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://www.aemet.es/xml/municipios/localidad_46250.xml"  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 0  
  },  
  "validity": {  
    "type": "Text",  
    "value": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00"  
  },  
  "dateIssued": {  
    "type": "DateTime",  
    "value": "2016-12-01T10:40:01.00Z"  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "Spain",  
      "postalCode": "46005",  
      "addressLocality": "Valencia"  
    }  
  },  
  "dateRetrieved": {  
    "type": "DateTime",  
    "value": "2016-12-01T12:57:24.00Z"  
  },  
  "validFrom": {  
    "type": "DateTime",  
    "value": "2016-12-01T17:00:00.00Z"  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 0.85  
  },  
  "uVIndexMax": {  
    "type": "Number",  
    "value": 1.00  
  }  
}  
```  
</details>  
#### WeatherForecast NGSI-LD key-values Example    
Here is an example of a WeatherForecast in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WeatherForecast:Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
    "type": "WeatherForecast",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "Spain",  
            "postalCode": "46005",  
            "addressLocality": "Valencia",  
            "type": "PostalAddress"  
        }  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "TEF"  
    },  
    "dateIssued": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T10:40:01.00Z"  
        }  
    },  
    "dateRetrieved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T12:57:24.00Z"  
        }  
    },  
    "dayMaximum": {  
        "type": "Property",  
        "value": {  
            "feelsLikeTemperature": 15,  
            "temperature": 15,  
            "relativeHumidity": 0.9  
        }  
    },  
    "dayMinimum": {  
        "type": "Property",  
        "value": {  
            "feelsLikeTemperature": 11,  
            "temperature": 11,  
            "relativeHumidity": 0.7  
        }  
    },  
    "feelsLikeTemperature": {  
        "type": "Property",  
        "value": 12  
    },  
    "precipitationProbability": {  
        "type": "Property",  
        "value": 0.15  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.85  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://www.aemet.es/xml/municipios/localidad_46250.xml"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12  
    },  
    "uvIndexMax": {  
        "type": "Property",  
        "value": 1.0  
    },  
    "validFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T17:00:00.00Z"  
        }  
    },  
    "validTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T23:00:00.00Z"  
        }  
    },  
    "validity": {  
        "type": "Property",  
        "value": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00"  
    },  
    "weatherType": {  
        "type": "Property",  
        "value": "overcast"  
    },  
    "windSpeed": {  
        "type": "Property",  
        "value": 0  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### WeatherForecast NGSI-LD normalized Example    
Here is an example of a WeatherForecast in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
    "type": "WeatherForecast",  
    "address": {  
        "type": "PostalAddress",  
        "value": {  
            "addressCountry": "Spain",  
            "postalCode": "46005",  
            "addressLocality": "Valencia"  
        }  
    },  
    "dataProvider": {  
        "type": "Text",  
        "value": "TEF"  
    },  
    "dateIssued": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T10:40:01.00Z"  
        }  
    },  
    "dateRetrieved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T12:57:24.00Z"  
        }  
    },  
    "dayMaximum": {  
        "type": "Property",  
        "value": {  
            "feelsLikeTemperature": 15,  
            "temperature": 15,  
            "relativeHumidity": 0.9  
        }  
    },  
    "dayMinimum": {  
        "type": "Property",  
        "value": {  
            "feelsLikeTemperature": 11,  
            "temperature": 11,  
            "relativeHumidity": 0.7  
        }  
    },  
    "feelsLikeTemperature": {  
        "type": "Property",  
        "value": 12  
    },  
    "precipitationProbability": {  
        "type": "Property",  
        "value": 0.15  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.85  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://www.aemet.es/xml/municipios/localidad_46250.xml"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12  
    },  
    "uVIndexMax": {  
        "type": "Property",  
        "value": 1.0  
    },  
    "validFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T17:00:00.00Z"  
        }  
    },  
    "validTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T23:00:00.00Z"  
        }  
    },  
    "validity": {  
        "type": "Property",  
        "value": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00"  
    },  
    "weatherType": {  
        "type": "Text",  
        "value": "overcast"  
    },  
    "windSpeed": {  
        "type": "Property",  
        "value": 0  
    },  
    "@context": [  
        "https://smartdatamdels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
