Entité : Prévisions météorologiques  
===================================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherForecast/LICENSE.md)  
Description globale : **Description harmonisée d'une prévision météorologique**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateIssued`: La date et l'heure auxquelles la prévision a été émise par le bureau météorologique au format ISO8601 UTC.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateRetrieved`: La date et l'heure de la prévision ont été récupérées au format ISO8601 UTC.  - `dayMaximum`: Valeurs maximales pour la période couverte par le rapport. Sous-attributs:- "température" : température maximale. Voir `WeatherForecast.temperature` pour la description et les unités. - FeelLikesTemperature". Maximum ressemble à la température. Même sémantique et unités que pour le fichier `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Humidité relative maximale. Même sémantique et mêmes unités que pour "WeatherForecast.relativeHumidity".  - `dayMinimum`: Valeurs minimales prévues pour la période couverte par le rapport.  Valeurs minimales pour la période couverte par le rapport. Sous-attributs:- `temperature` : Température minimale. Voir `WeatherForecast.temperature` pour la description et les unités. - FeelLikesTemperature". Température minimale ressentie. Même sémantique et unités que pour le fichier `WeatherForecast.feelLikeTemperature`.- `relativeHumidity`. Humidité relative minimale. Même sémantique et unités que pour "WeatherForecast.relativeHumidity".  - `description`: Une description de cet article  - `feelLikesTemperature`: Appréciation de la température de l'objet  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refPointOfInterest`: Point d'intérêt lié à l'article  - `relativeHumidity`: Humidité de l'air  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `temperature`: Température de l'objet  - `type`: Type d'entité NGSI. Il doit s'agir de WeatherForecast  - `uVIndexMax`: L'indice UV maximum pour la période, basé sur la mesure de l'indice UV de l'Organisation mondiale de la santé. Références normatives : [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  - `validFrom`: Date et heure de début de la période de validité.  - `validTo`: Date et heure de fin de la période de validité.  - `validity`: Inclut la période de validité de cette prévision comme un intervalle de temps ISO8601. Pour pallier le manque de prise en charge d'Orion Context Broker pour les intervalles date-heure, il peut être utilisé avec deux attributs distincts : validFrom, validTo.  - `visibility`: Catégories de visibilité  - `weatherType`: Description textuelle de la météo  - `windDirection`: Pari sur la direction du vent  - `windSpeed`: Intensité du vent    
Propriétés requises  
- `address`  - `dateIssued`  - `id`  - `type`    
Cette entité est principalement associée aux segments verticaux de l'environnement et de l'agriculture mais s'applique à de nombreuses applications différentes. Ce modèle de données a été développé en coopération avec les opérateurs de téléphonie mobile et la [GSMA] (https://www.gsma.com/iot/iot-big-data/).  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherForecast:    
  description: 'A harmonised description of a Weather Forecast'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateIssued:    
      description: 'The date and time the forecast was issued by the meteorological bureau in ISO8601 UTC format.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateRetrieved:    
      description: 'The date and time the forecast was retrieved in ISO8601 UTC format.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dayMaximum:    
      allOf:    
        - description: 'Property. Air conditions categories'    
          properties: &properties    
            feelLikesTemperature:    
              description: 'Property. Temperature appreciation of the item'    
              type: number    
            relativeHumidity:    
              description: 'Property. Humidity in the Air'    
              maximum: 1    
              minimum: 0    
              type: number    
            temperature:    
              description: 'Property. Temperature of the item'    
              type: number    
          type: object    
      description: 'Maximum values for the reported period. Subattributes:- `temperature` : Maximum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Maximum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.-   `relativeHumidity`. Maximum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
    dayMinimum:    
      allOf:    
        - description: 'Property. Air conditions categories'    
          properties: *properties    
          type: object    
      description: 'Minimum values forecasted for the reported period.  Minimum values for the reported period. Subattributes:- `temperature` : Minimum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Minimum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Minimum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    description:    
      description: 'A description of this item'    
      type: Property    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
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
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *weatherforecast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refPointOfInterest:    
      description: 'Point of interest related to the item'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    relativeHumidity:    
      description: 'Humidity in the Air'    
      maximum: 1    
      minimum: 0    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    temperature:    
      description: 'Temperature of the item'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WeatherForecast'    
      enum:    
        - WeatherForecast    
      type: Property    
    uVIndexMax:    
      description: 'The maximum UV index for the period, based on the World Health Organization''s UV Index measure. Normative references: [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    validFrom:    
      description: 'Validity period start date and time.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    validTo:    
      description: 'Validity period end date and time.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `validFrom`, `validTo`.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    weatherType:    
      description: 'Text description of the weather'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text.    
    windDirection:    
      description: 'Direction of the wind bet'    
      maximum: 180    
      minimum: -180    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    windSpeed:    
      description: 'Intensity of the wind'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http//schema.org/Number    
  required:    
    - id    
    - type    
    - dateIssued    
    - address    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WeatherForecast NGSI V2 - Exemple de valeurs clés  
Voici un exemple de prévisions météorologiques au format JSON comme valeurs clés. Ce format est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### WeatherForecast NGSI V2 normalisé Exemple  
Voici un exemple de prévision météorologique au format JSON normalisé. Ce format est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
  "type": "WeatherForecast",  
  "dayMinimum": {  
    "value": {  
      "feelsLikeTemperature": 11,  
      "temperature": 11,  
      "relativeHumidity": 0.7  
    }  
  },  
  "feelsLikeTemperature": {  
    "value": 12  
  },  
  "dataProvider": {  
    "value": "TEF"  
  },  
  "temperature": {  
    "value": 12  
  },  
  "validTo": {  
    "type": "DateTime",  
    "value": "2016-12-01T23:00:00.00Z"  
  },  
  "weatherType": {  
    "value": "overcast"  
  },  
  "precipitationProbability": {  
    "value": 0.15  
  },  
  "dayMaximum": {  
    "value": {  
      "feelsLikeTemperature": 15,  
      "temperature": 15,  
      "relativeHumidity": 0.9  
    }  
  },  
  "source": {  
    "value": "http://www.aemet.es/xml/municipios/localidad_46250.xml"  
  },  
  "windSpeed": {  
    "value": 0  
  },  
  "validity": {  
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
    "value": 0.85  
  },  
  "uVIndexMax": {  
    "value": 1.00  
  }  
}  
```  
#### WeatherForecast NGSI-LD valeurs clés Exemple  
Voici un exemple de prévisions météorologiques au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:WeatherForecast:Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
    "type": "WeatherForecast",  
    "dayMinimum": {  
      "feelsLikeTemperature": 11,  
      "temperature": 11,  
      "relativeHumidity": 0.7  
    },  
    "feelsLikeTemperature": 12,  
    "dataProvider": "TEF",  
    "temperature": 12,  
    "validTo": "2016-12-01T23:00:00.00Z",  
    "weatherType": "overcast",  
    "precipitationProbability": 0.15,  
    "dayMaximum":{  
      "feelsLikeTemperature": 15,  
      "temperature": 15,  
      "relativeHumidity": 0.9  
    },  
    "source": "http://www.aemet.es/xml/municipios/localidad_46250.xml",  
    "windSpeed": 0,  
    "validity": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00",  
    "dateIssued": "2016-12-01T10:40:01.00Z",  
    "address": {  
      "addressCountry": "Spain",  
      "postalCode": "46005",  
      "addressLocality": "Valencia",  
      "type": "PostalAddress"  
    },  
    "dateRetrieved": "2016-12-01T12:57:24.00Z",  
    "validFrom": "2016-12-01T17:00:00.00Z",  
    "relativeHumidity": 0.85,  
    "uvIndexMax": 1.00,  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld"  
    ]  
}  
```  
#### WeatherForecast NGSI-LD normalisé Exemple  
Voici un exemple de prévision météorologique au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:WeatherForecast:Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
    "type": "WeatherForecast",  
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
    "dataProvider": {  
        "type": "Property",  
        "value": "TEF"  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 12  
    },  
    "validTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T23:00:00.00Z"  
        }  
    },  
    "weatherType": {  
        "type": "Property",  
        "value": "overcast"  
    },  
    "precipitationProbability": {  
        "type": "Property",  
        "value": 0.15  
    },  
    "dayMaximum": {  
        "type": "Property",  
        "value": {  
            "feelsLikeTemperature": 15,  
            "temperature": 15,  
            "relativeHumidity": 0.9  
        }  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://www.aemet.es/xml/municipios/localidad_46250.xml"  
    },  
    "windSpeed": {  
        "type": "Property",  
        "value": 0  
    },  
    "validity": {  
        "type": "Property",  
        "value": "2016-12-01T18:00:00+01:00/2016-12-02T00:00:00+01:00"  
    },  
    "dateIssued": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T10:40:01.00Z"  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "Spain",  
            "postalCode": "46005",  
            "addressLocality": "Valencia",  
            "type": "PostalAddress"  
        }  
    },  
    "dateRetrieved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T12:57:24.00Z"  
        }  
    },  
    "validFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-01T17:00:00.00Z"  
        }  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.85  
    },  
    "uvIndexMax": {  
        "type": "Property",  
        "value": 1.00  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
