<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : WeatherForecast  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherForecast/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Description harmonisée d'une prévision météorologique**  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateIssued[date-time]`: La date et l'heure auxquelles la prévision a été émise par le bureau météorologique dans le format ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateRetrieved[date-time]`: La date et l'heure de la récupération de la prévision au format ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dayMaximum[object]`: Valeurs maximales pour la période considérée. Sous-attributs:- `temperature` : Température maximale. Voir `WeatherForecast.temperature` pour la description et les unités. - `feelLikesTemperature`. Température maximale ressentie. Même sémantique et mêmes unités que `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Humidité relative maximale. Même sémantique et mêmes unités que `WeatherForecast.relativeHumidity`  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `feelLikesTemperature[number]`: Appréciation de la température de l'objet    
	- `relativeHumidity[number]`: Humidité de l'air. Humidité relative instantanée observée (vapeur d'eau dans l'air)    
	- `temperature[number]`: Température de l'article    
- `dayMinimum[object]`: Valeurs minimales prévues pour la période considérée.  Valeurs minimales pour la période considérée. Sous-attributs:- `temperature` : Température minimale. Voir `WeatherForecast.temperature` pour la description et les unités. - `feelLikesTemperature`. Température minimale ressentie. Même sémantique et mêmes unités que `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Humidité relative minimale. Sémantique et unités identiques à celles de `WeatherForecast.relativeHumidity`.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `feelLikesTemperature[number]`: Appréciation de la température de l'objet    
	- `relativeHumidity[number]`: Humidité de l'air. Humidité relative instantanée observée (vapeur d'eau dans l'air)    
	- `temperature[number]`: Température de l'article    
- `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `precipitation[number]`: Quantité de pluie attendue  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de WeatherForecast  - `uVIndexMax[number]`: L'indice UV maximal pour la période, basé sur la mesure de l'indice UV de l'Organisation mondiale de la santé. Références normatives : [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  . Model: [https://schema.org/Number](https://schema.org/Number)- `validFrom[date-time]`: Date et heure de début de la période de validité  . Model: [https://schema.org/Text](https://schema.org/Text)- `validTo[date-time]`: Date et heure de fin de la période de validité  . Model: [https://schema.org/Text](https://schema.org/Text)- `validity[string]`: Inclut la période de validité de cette prévision en tant qu'intervalle de temps ISO8601. Pour pallier le manque de support d'Orion Context Broker pour les intervalles de temps, il est possible d'utiliser deux attributs distincts : `validFrom`, `validTo`.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `dateIssued`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Cette entité est principalement associée aux segments verticaux de l'environnement et de l'agriculture, mais elle est applicable à de nombreuses applications différentes. Ce modèle de données a été élaboré en collaboration avec les opérateurs de téléphonie mobile et la [GSMA] (https://www.gsma.com/iot/iot-big-data/).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherForecast:    
  description: A harmonised description of a Weather Forecast    
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
    dateIssued:    
      description: The date and time the forecast was issued by the meteorological bureau in ISO8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateRetrieved:    
      description: The date and time the forecast was retrieved in ISO8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dayMaximum:    
      description: 'Maximum values for the reported period. Subattributes:- `temperature` : Maximum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Maximum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.-   `relativeHumidity`. Maximum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`'    
      properties:    
        feelLikesTemperature:    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dayMinimum:    
      description: 'Minimum values forecasted for the reported period.  Minimum values for the reported period. Subattributes:- `temperature` : Minimum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Minimum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Minimum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`'    
      properties:    
        feelLikesTemperature:    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
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
      description: Amount of water rain expected    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be WeatherForecast    
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
      description: Validity period start date and time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    validTo:    
      description: Validity period end date and time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `validFrom`, `validTo`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - dateIssued    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherForecast/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### WeatherForecast NGSI-v2 valeurs-clés Exemple  
Voici un exemple de prévisions météorologiques au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### WeatherForecast NGSI-v2 normalisé Exemple  
Voici un exemple de prévision météorologique au format JSON-LD normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
    "type": "Boolean",  
    "value": false  
  },  
  "validity": {  
    "type": "DateTime",  
    "value": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00"  
  },  
  "dateIssued": {  
    "type": "DateTime",  
    "value": "2016-12-01T10:40:01.00Z"  
  },  
  "address": {  
    "type": "StructuredValue",  
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
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>  
#### WeatherForecast Valeurs clés NGSI-LD Exemple  
Voici un exemple de prévisions météorologiques au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  "uVIndexMax": 1,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### WeatherForecast NGSI-LD normalisé Exemple  
Voici un exemple de prévision météorologique au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
  "type": "WeatherForecast",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "Spain",  
      "postalCode": "46005",  
      "addressLocality": "Valencia"  
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
    "type": "Property",  
    "value": "overcast"  
  },  
  "windSpeed": {  
    "type": "Property",  
    "value": 0  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
