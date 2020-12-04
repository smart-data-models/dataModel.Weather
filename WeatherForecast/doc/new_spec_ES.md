Entidad: Pronóstico del tiempo  
==============================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Una descripción armonizada de un pronóstico del tiempo**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateIssued`: La fecha y la hora en que el pronóstico fue emitido por la oficina meteorológica en formato ISO8601 UTC.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateRetrieved`: La fecha y la hora en que el pronóstico fue recuperado en formato ISO8601 UTC.  - `dayMaximum`: Valores máximos para el período de que se informa. Subatributos:- `temperatura` : Temperatura máxima. Ver "Pronóstico del tiempo. Temperatura" para la descripción y las unidades. - "Sensación de temperatura". Máximo se siente como temperatura. La misma semántica y unidades que en "Pronóstico del tiempo, temperatura similar a la de la temperatura". - "Humedad relativa". Máxima humedad relativa. La misma semántica y unidades que "Pronóstico del tiempo. Humedad relativa".  - `dayMinimum`: Valores mínimos previstos para el período de que se informa.  Valores mínimos previstos para el período objeto de informe. Subatributos:- `temperatura` : Temperatura mínima. Ver "Pronóstico del tiempo. Temperatura" para la descripción y las unidades. - `feelLikesTemperature`. El mínimo se siente como temperatura. La misma semántica y unidades que en "Pronóstico del tiempo, temperatura similar a la de la temperatura". - "Humedad relativa". Humedad relativa mínima. La misma semántica y unidades que "Pronóstico del tiempo. Humedad relativa".  - `description`: Una descripción de este artículo  - `feelLikesTemperature`: Apreciación de la temperatura del objeto  - `id`:   - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refPointOfInterest`: Punto de interés relacionado con el artículo  - `relativeHumidity`: La humedad en el aire  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `temperature`: La temperatura del objeto  - `type`: Tipo de entidad NGSI. Tiene que ser el Pronóstico del Tiempo  - `uVIndexMax`: El índice UV máximo del período, basado en la medida del índice UV de la Organización Mundial de la Salud. Referencias normativas: [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  - `validFrom`: Fecha y hora de inicio del período de validez.  - `validTo`: Fecha y hora de finalización del período de validez.  - `validity`: Incluye el período de validez de esta previsión como un intervalo de tiempo ISO8601. Como solución para la falta de apoyo del Orion Context Broker para los intervalos de tiempo de fecha, se pueden utilizar dos atributos separados: "ValidFrom", "ValidTo".  - `visibility`: Categorías de visibilidad  - `weatherType`: La descripción de texto del tiempo  - `windDirection`: Dirección de la apuesta de viento  - `windSpeed`: La intensidad del viento    
Propiedades requeridas  
- `address`  - `dateIssued`  - `id`  - `type`    
Esta entidad se asocia principalmente con los segmentos verticales del medio ambiente y la agricultura, pero es aplicable a muchas aplicaciones diferentes. Este modelo de datos se ha desarrollado en cooperación con los operadores de telefonía móvil y la [GSMA] (https://www.gsma.com/iot/iot-big-data/).  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherForecast:    
  description: 'A harmonised description of a Weather Forecast'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
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
## Ejemplo de cargas útiles  
#### Pronóstico del tiempo NGSI V2 Ejemplo de valores clave  
Aquí hay un ejemplo de un Pronóstico del Tiempo en formato JSON como valores clave. Es compatible con NGSI V2 cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### Pronóstico del tiempo Ejemplo normalizado NGSI V2  
Aquí hay un ejemplo de un Pronóstico del Tiempo en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Pronóstico del Tiempo NGSI-LD Ejemplo de valores clave  
Aquí hay un ejemplo de un Pronóstico del Tiempo en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### Pronóstico del tiempo Ejemplo normalizado NGSI-LD  
Aquí hay un ejemplo de un Pronóstico del Tiempo en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
