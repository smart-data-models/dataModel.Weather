<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: WeatherObserved  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Beobachtung der Wetterbedingungen an einem bestimmten Ort und zu einer bestimmten Zeit. Dieses Datenmodell wurde in Zusammenarbeit mit Mobilfunkbetreibern und der GSMA entwickelt.**  
Version: 0.3.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `airQualityIndex[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Der Luftqualitätsindex ist eine Zahl, die verwendet wird, um die Qualität der Luft an einem bestimmten Tag anzugeben.  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityIndexForecast[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Prognostizierter Gesamtluftqualitätsindex (AQI) über einen bestimmten Zeitraum in der Zukunft.  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureForecast[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Prognostizierter Wert der Lufttemperatur über einen bestimmten Zeitraum in der Zukunft.  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureTSA[object]`: Eigenschaft. Aggregation von Lufttemperatur-Zeitreihen  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `aqiMajorPollutant[string]`: Eigenschaft. Modell:'https://schema.org/Text'. Hauptschadstoff im Luftqualitätsindex (AQI).  . Model: [https://schema.org/Text](https://schema.org/Text)- `aqiMajorPollutantForecast[string]`: Eigenschaft. Modell:'https://schema.org/Text'. Prognostizierter Hauptluftschadstoff im Luftqualitätsindex (AQI) über einen bestimmten Zeitraum in der Zukunft.  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: Der beobachtete atmosphärische Druck, gemessen in Hecto-Pascal  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateObserved[string]`: Datum der vom Benutzer definierten beobachteten Einheit.  - `description[string]`: Eine Beschreibung dieses Artikels  - `dewPoint[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Einheiten:'Celsius Grad'. Der als Zahl kodierte Taupunkt. Beobachtete Temperatur, auf die Luft abgekühlt werden muss, um mit Wasserdampf gesättigt zu werden  . Model: [https://schema.org/Number](https://schema.org/Number)- `diffuseIrradiation[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Die diffuse Bestrahlungsstärke ist der Teil der Sonneneinstrahlung, der von der Atmosphäre gestreut wird. Einheiten:'w/m2'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `directIrradiation[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Die direkte Bestrahlungsstärke ist der Teil der Sonneneinstrahlung, der direkt auf eine Oberfläche trifft. Einheiten:'w/m2'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `feelLikesTemperature[number]`: Bewertung der Temperatur des Gegenstands  - `gustSpeed[number]`: Ein plötzlicher Ausbruch von Wind mit hoher Geschwindigkeit, der die beobachtete durchschnittliche Windgeschwindigkeit übersteigt und nur wenige Sekunden dauert.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `illuminance[number]`: Eigenschaft. Beobachtete momentane Umgebungslichtintensität. Einheiten:'Lux'  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `precipitation[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Menge des registrierten Wasserregens. Einheiten:'Liter pro Quadratmeter'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationForecast[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Prognostizierter Niederschlag für eine bestimmte Dauer in der Zukunft.  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressureTendency[*]`: Eigenschaft. Enum:'fallend, steigend, gleichbleibend'. Steigt oder fällt der Druck? Er kann quantitativ oder qualitativ ausgedrückt werden.  - `refDevice[*]`: Verwandtschaft. Modell:'https://schema.org/URL'. Ein Verweis auf das/die Gerät(e), das/die diese Beobachtung aufgezeichnet hat/haben.  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[string]`: Interessanter Punkt im Zusammenhang mit dem Artikel  . Model: [http://schema.org/URL](http://schema.org/URL)- `relativeHumidity[number]`: Feuchte in der Luft. Beobachtete momentane relative Luftfeuchtigkeit (Wasserdampf in der Luft)  - `relativeHumidityForecast[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Prognostizierte relative Luftfeuchtigkeit (Wasserdampf in der Luft) über einen bestimmten Zeitraum in der Zukunft  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `snowHeight[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Die von generischen Schneehöhenmesssensoren beobachtete Schneehöhe, ausgedrückt in Zentimetern. Einheiten:'Zentimeter'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `solarRadiation[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Die beobachtete Sonneneinstrahlung, gemessen in Watt pro Quadrat. Einheiten:'w/m2'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `streamGauge[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Die von hydrometrischen Messsensoren, d. h. einem [Strompegel](https://en.wikipedia.org/wiki/Stream_gauge), beobachtete Wasserstandshöhe, ausgedrückt in Zentimetern. Einheiten:'centimeters'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: Temperatur des Gegenstandes  - `type[string]`: Eigenschaft. NGSI-Entitätstyp. Es muss WeatherObserved sein  - `uVIndexMax[number]`: Eigenschaft. Modell:'https://schema.org/Number'. Der maximale UV-Index für den Zeitraum, basierend auf der UV-Index-Messung der Weltgesundheitsorganisation. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) sind die Werte zwischen 1 und 11 der gültige Bereich für den Index. Der Wert 0 bedeutet, dass kein Signal erkannt wurde und daher kein Wert gespeichert wird.  . Model: [https://schema.org/Number](https://schema.org/Number)- `visibility[*]`: Kategorien der Sichtbarkeit  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: Textbeschreibung des Wetters  . Model: [http://schema.org/Text.](http://schema.org/Text.)- `windDirection[number]`: Wette auf die Windrichtung  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: Intensität des Windes  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Windrichtungsbereich gemäß der [Weltorganisation für Meteorologie] (https://library.wmo.int/doc_num.php?explnum_id=3177)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    airQualityIndex:    
      description: 'Property. Model:''https://schema.org/Number''. Air quality index is a number used to report the quality of the air on any given day.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityIndexForecast:    
      description: 'Property. Model:''https://schema.org/Number''. Forecasted overall Air Quality Index (AQI) over a certain duration in future.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airTemperatureForecast:    
      description: 'Property. Model:''https://schema.org/Number''. Forecasted value of air temperature over a certain duration in future.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airTemperatureTSA:    
      description: Property. Air temperature time series aggregation    
      properties:    
        averageValue:    
          type: number    
        instValue:    
          type: number    
        maxOverTime:    
          type: number    
        minOverTime:    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    aqiMajorPollutant:    
      description: 'Property. Model:''https://schema.org/Text''. Major pollutant in the Air Quality Index (AQI).'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    aqiMajorPollutantForecast:    
      description: 'Property. Model:''https://schema.org/Text''. Forecasted major air pollutant in the Air Quality Index (AQI) over a certain duration in future.'    
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
    atmosphericPressure:    
      description: The atmospheric pressure observed measured in Hecto Pascals    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hecto pascals    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: Date of the observed entity defined by the user.    
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
      description: 'Property. Model:''https://schema.org/Number''. Units:''Celsius degrees''. The dew point encoded as a number. Observed temperature to which air must be cooled to become saturated with water vapor'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Celsius degrees    
    diffuseIrradiation:    
      description: 'Property. Model:''https://schema.org/Number''. Diffuse irradiance is the part of the solar irradiance that is scattered by the atmosphere. Units:''w/m2'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: w/m2    
    directIrradiation:    
      description: 'Property. Model:''https://schema.org/Number''. Direct irradiance is the part of the solar irradiance that directly reaches a surface. Units:''w/m2'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: w/m2    
    feelLikesTemperature:    
      description: Temperature appreciation of the item    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &weatherobserved_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    illuminance:    
      description: 'Property. Observed instantaneous ambient light intensity. Units:''Lux'''    
      type: number    
      x-ngsi:    
        type: Property    
        units: Lux    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *weatherobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: 'Property. Model:''https://schema.org/Number''. Amount of water rain registered. Units:''Liters per square meter''. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter    
    precipitationForecast:    
      description: 'Property. Model:''https://schema.org/Number''. Forecasted rainfall over a certain duration in future.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pressureTendency:    
      description: 'Property. Enum:''falling, raising, steady''. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms.'    
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
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: 'Relationship. Model:''https://schema.org/URL''. A reference to the device(s) which captured this observation.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refPointOfInterest:    
      description: Point of interest related to the item    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    relativeHumidity:    
      description: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    relativeHumidityForecast:    
      description: 'Property. Model:''https://schema.org/Number''. Forecasted relative humidity (water vapour in air) over a certain duration in future'    
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
      description: 'Property. Model:''https://schema.org/Number''. The snow height observed by generic snow depth measurement sensors, expressed in centimeters. Units:''centimeters'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: centimeters    
    solarRadiation:    
      description: 'Property. Model:''https://schema.org/Number''. The solar radiation observed measured in Watts per square. Units:''w/m2'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: w/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    streamGauge:    
      description: 'Property. Model:''https://schema.org/Number''. The water level surface elevation observed by Hydrometric measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expressed in centimeters. Units:''centimeters'''    
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
      description: Property. NGSI Entity type. It has to be WeatherObserved    
      enum:    
        - WeatherObserved    
      type: string    
      x-ngsi:    
        type: Property    
    uVIndexMax:    
      description: 'Property. Model:''https://schema.org/Number''. The maximum UV index for the period, based on the World Health Organization''s UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) the values between 1 and 11 are the valid range for the index. The value 0 is for describing that no signal is detected so no value is stored.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: Categories of visibility    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    weatherType:    
      description: Text description of the weather    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text.    
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
## Beispiel-Nutzlasten  
#### WeatherObserved NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein WeatherObserved im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WetterObserviert NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein WeatherObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "type": "Number",  
    "value": 0  
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
    "type": "Relationship",  
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
    "type": "PostalAddress",  
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
    "type": "Number",  
    "value": 1  
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
    "type": "Number",  
    "value": 1.0  
  }  
}  
```  
</details>  
#### Wetterbeobachtete NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein WeatherObserved im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WetterObserviert NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein WeatherObserved im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
    "type": "WeatherObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Valladolid",  
            "addressCountry": "ES",  
            "type": "PostalAddress"  
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
        "https://smart-data-models.github.io/dataModel.Weather/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
