<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : MétéoObservée  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Observation des conditions météorologiques à un endroit et à un moment donnés. Ce modèle de données a été développé en coopération avec les opérateurs de téléphonie mobile et la GSMA.  
version : 0.3.3  
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
- `airQualityIndex[number]`: L'indice de qualité de l'air est un nombre utilisé pour indiquer la qualité de l'air un jour donné.  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityIndexForecast[number]`: Indice global de qualité de l'air (IQA) prévu pour une certaine durée à l'avenir  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureForecast[number]`: Valeur prévue de la température de l'air sur une certaine durée dans le futur  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureTSA[object]`: Agrégation des séries temporelles de la température de l'air  	- `averageValue[number]`: Valeur moyenne du traitement temporel dans le temps    
	- `instValue[number]`: Valeur instantanée du traitement temporel    
	- `maxOverTime[number]`: Valeur maximale du traitement temporel dans le temps    
	- `minOverTime[number]`: Valeur minimale du traitement temporel dans le temps    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `aqiMajorPollutant[string]`: Principal polluant de l'indice de qualité de l'air (IQA)  . Model: [https://schema.org/Text](https://schema.org/Text)- `aqiMajorPollutantForecast[string]`: Principaux polluants atmosphériques prévus dans l'indice de qualité de l'air (IQA) sur une certaine durée à l'avenir  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: La pression atmosphérique observée est mesurée en Hecto Pascals.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateObserved[date-time]`: Date de l'entité observée définie par l'utilisateur  - `description[string]`: Une description de l'article  - `dewPoint[number]`: Le point de rosée codé sous forme de nombre. Température observée à laquelle l'air doit être refroidi pour devenir saturé en vapeur d'eau.  . Model: [https://schema.org/Number](https://schema.org/Number)- `diffuseIrradiation[number]`: L'irradiation diffuse est la partie de l'irradiation solaire qui est dispersée par l'atmosphère.  . Model: [https://schema.org/Number](https://schema.org/Number)- `directIrradiation[number]`: L'irradiation directe est la partie de l'irradiation solaire qui atteint directement une surface.  . Model: [https://schema.org/Number](https://schema.org/Number)- `feelLikesTemperature[number]`: Appréciation de la température de l'objet  - `gustSpeed[number]`: Une rafale soudaine de vent à grande vitesse dépassant la vitesse moyenne observée et ne durant que quelques secondes.  - `id[*]`: Identifiant unique de l'entité  - `illuminance[number]`: Intensité lumineuse ambiante instantanée observée  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `precipitation[number]`: Quantité d'eau de pluie enregistrée.  . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationForecast[number]`: Prévision des précipitations sur une certaine durée dans le futur  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressureTendency[*]`: Enum : "en baisse, en hausse, stable". La pression augmente-t-elle ou diminue-t-elle ? Elle peut être exprimée en termes quantitatifs ou qualitatifs  - `refDevice[*]`: Une référence au(x) dispositif(s) qui a(ont) capturé cette observation  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[string]`: Point d'intérêt lié à l'objet  . Model: [http://schema.org/URL](http://schema.org/URL)- `relativeHumidity[number]`: Humidité de l'air. Humidité relative instantanée observée (vapeur d'eau dans l'air)  - `relativeHumidityForecast[number]`: Prévision de l'humidité relative (vapeur d'eau dans l'air) sur une certaine durée dans le futur  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `snowHeight[number]`: Hauteur de neige observée par les capteurs génériques de mesure de l'épaisseur de la neige, exprimée en centimètres.  . Model: [https://schema.org/Number](https://schema.org/Number)- `solarRadiation[number]`: Le rayonnement solaire observé est mesuré en watts par mètre carré.  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `streamGauge[number]`: L'élévation de la surface du niveau de l'eau observée par les capteurs de mesure hydrométrique, à savoir un [Stream Gauge] (https://en.wikipedia.org/wiki/Stream_gauge), exprimée en centimètres.  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: Température de l'article  - `type[string]`: Type d'entité NGSI. Il doit s'agir de WeatherObserved  - `uVIndexMax[number]`: L'indice UV maximal pour la période, basé sur la mesure de l'indice UV de l'Organisation mondiale de la santé. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) Les valeurs comprises entre 1 et 11 constituent la plage de validité de l'indice. La valeur 0 indique qu'aucun signal n'a été détecté et qu'aucune valeur n'est donc enregistrée.  . Model: [https://schema.org/Number](https://schema.org/Number)- `visibility[*]`: Catégories de visibilité  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: Description textuelle du temps  . Model: [http://schema.org/Text](http://schema.org/Text)- `windDirection[number]`: Direction du vent pari  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: Intensité du vent  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Plage de direction du vent définie selon l'[Organisation météorologique mondiale] (https://library.wmo.int/doc_num.php?explnum_id=3177)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
    atmosphericPressure:    
      description: The atmospheric pressure observed measured in Hecto Pascals    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hecto pascals    
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
    feelsLikeTemperature:    
      description: Temperature appreciation of the item    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds    
      type: number    
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
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherObserved/schema.json    
  x-model-tags: IUDX    
  x-version: 0.3.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Valeurs-clé de l'INS-v2 WeatherObserved Exemple  
Voici un exemple de WeatherObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  "temperature": 3.3,  
  "windDirection": 135,  
  "windSpeed": 2,  
  "illuminance": 1000,  
  "refDevice": "device-0A3478",  
  "streamGauge": 50,  
  "snowHeight": 20,  
  "uVIndexMax": 1.0  
}  
```  
</details>  
#### WeatherObserved NGSI-v2 normalisé Exemple  
Voici un exemple de WeatherObserved au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
    "value": 0.1  
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
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES"  
    }  
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
    "value": 0.15  
  },  
  "streamGauge": {  
    "type": "Number",  
    "value": 50  
  },  
  "snowHeight": {  
    "type": "Number",  
    "value": 20  
  },  
  "uVIndexMax": {  
    "type": "Number",  
    "value": 1.0  
  }  
}  
```  
</details>  
#### Valeurs clés de l'INS-LD pour les observations météorologiques Exemple  
Voici un exemple de WeatherObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  "streamGauge": 50,  
  "temperature": 3.3,  
  "uVIndexMax": 1.0,  
  "windDirection": 135,  
  "windSpeed": 2,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Weather/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### WeatherObserved NGSI-LD normalisé Exemple  
Voici un exemple de WeatherObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
  "streamGauge": {  
    "type": "Property",  
    "value": 50  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 3.3  
  },  
  "uVIndexMax": {  
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
