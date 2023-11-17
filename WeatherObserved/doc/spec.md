<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: WeatherObserved    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **An observation of weather conditions at a certain place and time. This data model has been developed in cooperation with mobile operators and the GSMA.**    
version: 0.3.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `airQualityIndex[number]`: Air quality index is a number used to report the quality of the air on any given day  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityIndexForecast[number]`: Forecasted overall Air Quality Index (AQI) over a certain duration in future  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureForecast[number]`: Forecasted value of air temperature over a certain duration in future  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureTSA[object]`: Air temperature time series aggregation  	- `averageValue[number]`: Average value of temporal processing over time      
	- `instValue[number]`: Instant value of temporal processing      
	- `maxOverTime[number]`: Maximum value of temporal processing over time      
- `alternateName[string]`: An alternative name for this item  - `aqiMajorPollutant[string]`: Major pollutant in the Air Quality Index (AQI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `aqiMajorPollutantForecast[string]`: Forecasted major air pollutant in the Air Quality Index (AQI) over a certain duration in future  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateObserved[date-time]`: Date of the observed entity defined by the user  - `description[string]`: A description of this item  - `dewPoint[number]`: The dew point encoded as a number. Observed temperature to which air must be cooled to become saturated with water vapor  . Model: [https://schema.org/Number](https://schema.org/Number)- `diffuseIrradiation[number]`: Diffuse irradiance is the part of the solar irradiance that is scattered by the atmosphere  . Model: [https://schema.org/Number](https://schema.org/Number)- `directIrradiation[number]`: Direct irradiance is the part of the solar irradiance that directly reaches a surface  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Unique identifier of the entity  - `illuminance[number]`: Observed instantaneous ambient light intensity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `precipitation[number]`: Amount of water rain registered.   . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationForecast[number]`: Forecasted rainfall over a certain duration in future  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressureTendency[*]`: Enum:'falling, raising, steady'. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms  - `refDevice[*]`: A reference to the device(s) which captured this observation  . Model: [https://schema.org/URL](https://schema.org/URL)- `relativeHumidity[number]`: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)  - `relativeHumidityForecast[number]`: Forecasted relative humidity (water vapour in air) over a certain duration in future  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `snowHeight[number]`: The snow height observed by generic snow depth measurement sensors, expressed in centimeters  . Model: [https://schema.org/Number](https://schema.org/Number)- `solarRadiation[number]`: The solar radiation observed measured in Watts per square  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `streamGauge[number]`: The water level surface elevation observed by Hydrometric measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expressed in centimeters  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: Temperature of the item  - `type[string]`: NGSI Entity type. It has to be WeatherObserved  - `uVIndexMax[number]`: The maximum UV index for the period, based on the World Health Organization's UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) the values between 1 and 11 are the valid range for the index. The value 0 is for describing that no signal is detected so no value is stored  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Wind direction range defined according to the [World Meteorological organization](https://library.wmo.int/doc_num.php?explnum_id=3177)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WeatherObserved:      
  description: An observation of weather conditions at a certain place and time. This data model has been developed in cooperation with mobile operators and the GSMA.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    airQualityIndex:      
      description: Air quality index is a number used to report the quality of the air on any given day      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    airQualityIndexForecast:      
      description: Forecasted overall Air Quality Index (AQI) over a certain duration in future      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    airTemperatureForecast:      
      description: Forecasted value of air temperature over a certain duration in future      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    airTemperatureTSA:      
      description: Air temperature time series aggregation      
      properties:      
        averageValue:      
          description: Average value of temporal processing over time      
          type: number      
          x-ngsi:      
            type: Property      
        instValue:      
          description: Instant value of temporal processing      
          type: number      
          x-ngsi:      
            type: Property      
        maxOverTime:      
          description: Maximum value of temporal processing over time      
          type: number      
          x-ngsi:      
            type: Property      
        minOverTime:      
          description: Minimum value of temporal processing over time      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    allOf:      
      - feelLikesTemperature:      
          description: Temperature appreciation of the item      
          type: number      
          x-ngsi:      
            type: Property      
        relativeHumidity:      
          description: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        temperature:      
          description: Temperature of the item      
          type: number      
          x-ngsi:      
            type: Property      
      - atmosphericPressure:      
          description: The atmospheric pressure observed measured in Hecto Pascals      
          minimum: 0      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
            units: Hecto pascals      
        gustSpeed:      
          description: A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds      
          type: number      
          x-ngsi:      
            type: Property      
        illuminance:      
          description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2)'      
          minimum: 0      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        refPointOfInterest:      
          description: Point of interest related to the item      
          type: string      
          x-ngsi:      
            model: http://schema.org/URL      
            type: Relationship      
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
          description: Categories of visibility      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        weatherType:      
          description: Text description of the weather      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        windDirection:      
          description: Direction of the wind bet      
          maximum: 360      
          minimum: 0      
          type: number      
          x-ngsi:      
            model: http://schema.org/Number      
            type: Property      
        windSpeed:      
          description: Intensity of the wind      
          minimum: 0      
          type: number      
          x-ngsi:      
            model: http//schema.org/Number      
            type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    aqiMajorPollutant:      
      description: Major pollutant in the Air Quality Index (AQI)      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    aqiMajorPollutantForecast:      
      description: Forecasted major air pollutant in the Air Quality Index (AQI) over a certain duration in future      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObserved:      
      description: Date of the observed entity defined by the user      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    dewPoint:      
      description: The dew point encoded as a number. Observed temperature to which air must be cooled to become saturated with water vapor      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Celsius degrees      
    diffuseIrradiation:      
      description: Diffuse irradiance is the part of the solar irradiance that is scattered by the atmosphere      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: w/m2      
    directIrradiation:      
      description: Direct irradiance is the part of the solar irradiance that directly reaches a surface      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: w/m2      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    illuminance:      
      description: Observed instantaneous ambient light intensity      
      type: number      
      x-ngsi:      
        type: Property      
        units: Lux      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    precipitation:      
      description: 'Amount of water rain registered. '      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Liters per square meter      
    precipitationForecast:      
      description: Forecasted rainfall over a certain duration in future      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    pressureTendency:      
      description: 'Enum:''falling, raising, steady''. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms'      
      oneOf:      
        - enum:      
            - falling      
            - raising      
            - steady      
          type: string      
        - type: number      
      x-ngsi:      
        type: Property      
    refDevice:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: A reference to the device(s) which captured this observation      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    relativeHumidity:      
      description: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    relativeHumidityForecast:      
      description: Forecasted relative humidity (water vapour in air) over a certain duration in future      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
    snowHeight:      
      description: 'The snow height observed by generic snow depth measurement sensors, expressed in centimeters'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: centimeters      
    solarRadiation:      
      description: The solar radiation observed measured in Watts per square      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: w/m2      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    streamGauge:      
      description: 'The water level surface elevation observed by Hydrometric measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expressed in centimeters'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: centimeters      
    temperature:      
      description: Temperature of the item      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be WeatherObserved      
      enum:      
        - WeatherObserved      
      type: string      
      x-ngsi:      
        type: Property      
    uVIndexMax:      
      description: 'The maximum UV index for the period, based on the World Health Organization''s UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) the values between 1 and 11 are the valid range for the index. The value 0 is for describing that no signal is detected so no value is stored'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
  required:      
    - id      
    - type      
    - dateObserved      
    - location      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherObserved/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherObserved/schema.json      
  x-model-tags: IUDX      
  x-version: 0.3.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### WeatherObserved NGSI-v2 key-values Example      
Here is an example of a WeatherObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
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
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ]  
  },  
  "precipitation": 0,  
  "pressureTendency": 0.5,  
  "relativeHumidity": 1,  
  "source": "http://www.aemet.es",  
  "stationCode": "2422",  
  "stationName": "Valladolid",  
  "temperature": 3.3,  
  "windDirection": 135,  
  "windSpeed": 2,  
  "illuminance": 1000,  
  "refDevice": "device-0A3478",  
  "streamGauge": 50,  
  "snowHeight": 20,  
  "uvIndexMax": 1.0  
}  
```  
</details>    
#### WeatherObserved NGSI-v2 normalized Example      
Here is an example of a WeatherObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Valladolid.2016-11-30T07-00-00.00Z",  
  "type": "WeatherObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2016-11-30T07:00:00.00Z"  
  },  
  "illuminance": {  
    "type": "Number",  
    "value": 1000  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 3.3  
  },  
  "precipitation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "atmosphericPressure": {  
    "type": "Number",  
    "value": 938.9  
  },  
  "pressureTendency": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "refDevice": {  
    "type": "Text",  
    "value": "device-0A3478"  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://www.aemet.es"  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.754444444,  
        41.640833333  
      ]  
    }  
  },  
  "stationName": {  
    "type": "Text",  
    "value": "Valladolid"  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES"  
    }  
  },  
  "stationCode": {  
    "type": "Text",  
    "value": "2422"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "TEF"  
  },  
  "windDirection": {  
    "type": "Number",  
    "value": 135  
  },  
  "relativeHumidity": {  
    "type": "Boolean",  
    "value": true  
  },  
  "streamGauge": {  
    "type": "Number",  
    "value": 50  
  },  
  "snowHeight": {  
    "type": "Number",  
    "value": 20  
  },  
  "uvIndexMax": {  
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### WeatherObserved NGSI-LD key-values Example      
Here is an example of a WeatherObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
  "type": "WeatherObserved",  
  "address": {  
    "addressLocality": "Valladolid",  
    "addressCountry": "ES"  
  },  
  "atmosphericPressure": 938.9,  
  "dataProvider": "TEF",  
  "dateObserved": "2016-11-30T07:00:00.00Z",  
  "illuminance": 1000,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ]  
  },  
  "precipitation": 0,  
  "pressureTendency": 0.5,  
  "refDevice": "urn:ngsi-ld:Device:device-0A3478",  
  "relativeHumidity": 1,  
  "snowHeight": 20,  
  "source": "http://www.aemet.es",  
  "stationCode": "2422",  
  "stationName": "Valladolid",  
  "streamGauge": 50,  
  "temperature": 3.3,  
  "uvIndexMax": 1.0,  
  "windDirection": 135,  
  "windSpeed": 2,  
  "@context": [  
    "iudx:EnvWeather",  
    "https://smart-data-models.github.io/dataModel.Weather/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WeatherObserved NGSI-LD normalized Example      
Here is an example of a WeatherObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
  "type": "WeatherObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES"  
    }  
  },  
  "atmosphericPressure": {  
    "type": "Property",  
    "value": 938.9  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "TEF"  
  },  
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
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.754444444,  
        41.640833333  
      ]  
    }  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": 0  
  },  
  "pressureTendency": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:device-0A3478"  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 1  
  },  
  "snowHeight": {  
    "type": "Property",  
    "value": 20  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.aemet.es"  
  },  
  "stationCode": {  
    "type": "Property",  
    "value": "2422"  
  },  
  "stationName": {  
    "type": "Property",  
    "value": "Valladolid"  
  },  
  "streamGauge": {  
    "type": "Property",  
    "value": 50  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 3.3  
  },  
  "uvIndexMax": {  
    "type": "Property",  
    "value": 1.0  
  },  
  "windDirection": {  
    "type": "Property",  
    "value": 135  
  },  
  "windSpeed": {  
    "type": "Property",  
    "value": 2  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Weather/context.jsonld"  
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
