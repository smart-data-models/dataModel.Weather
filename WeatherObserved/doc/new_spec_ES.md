Entidad: WeatherObserved  
========================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Una observación de las condiciones climáticas en un lugar y momento determinado. Este modelo de datos ha sido desarrollado en cooperación con los operadores móviles y el GSMA.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  - `atmosphericPressure`: La presión atmosférica observada medida en Hecto Pascals  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateObserved`: Fecha de la observación  - `description`: Una descripción de este artículo  - `dewPoint`: El punto de rocío codificado como un número  - `feelLikesTemperature`: Apreciación de la temperatura del objeto  - `id`:   - `illuminance`: (https://en.wikipedia.org/wiki/Illuminance) observados medidos en lux (lx) o lúmenes por metro cuadrado (cd-sr-m-2).  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `precipitation`: Temperatura del aire observada. Litros por metro cuadrado.  - `pressureTendency`: Enum: "cayendo, levantando, estable". ¿La presión está subiendo o bajando? Puede expresarse en términos cuantitativos o cualitativos.  - `refDevice`: Una referencia al dispositivo o dispositivos que capturaron esta observación.  - `refPointOfInterest`: Punto de interés relacionado con el artículo  - `relativeHumidity`: La humedad en el aire  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `snowHeight`: La altura de la nieve observada por los sensores genéricos de medición de la profundidad de la nieve, expresada en centímetros  - `solarRadiation`: La radiación solar observada medida en vatios por cuadrado  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `streamGauge`: La elevación de la superficie del nivel del agua observada por los sensores de medición hidrométrica, a saber, un [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expresado en centímetros  - `temperature`: La temperatura del objeto  - `type`: Tipo de entidad NGSI. Tiene que ser WeatherObserved  - `uVIndexMax`: El índice UV máximo del período, basado en la medida del índice UV de la Organización Mundial de la Salud. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  - `visibility`: Categorías de visibilidad  - `weatherType`: La descripción de texto del tiempo  - `windDirection`: Dirección de la apuesta de viento  - `windSpeed`: La intensidad del viento    
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherObserved:    
  description: 'An observation of weather conditions at a certain place and time. This data model has been developed in cooperation with mobile operators and the GSMA.'    
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
    atmosphericPressure:    
      description: 'The atmospheric pressure observed measured in Hecto Pascals'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Hecto pascals'    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      description: 'Date of the observation'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    dewPoint:    
      description: 'The dew point encoded as a number'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Celsius degrees'    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
      type: Property    
    id:    
      anyOf: &weatherobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
        anyOf: *weatherobserved_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    precipitation:    
      description: 'Air''s temperature observed. Liters per square meter. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    pressureTendency:    
      description: 'Enum:''falling, raising, steady''. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms.'    
      oneOf:    
        - enum:    
            - raising    
            - falling    
            - steady    
          type: string    
        - type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to the device(s) which captured this observation.'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
    snowHeight:    
      description: 'The snow height observed by generic snow depth measurement sensors, expressed in centimeters'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: centimeters    
    solarRadiation:    
      description: 'The solar radiation observed measured in Watts per square'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: w/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    streamGauge:    
      description: 'The water level surface elevation observed by Hydrometric measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expressed in centimeters'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: centimeters    
    temperature:    
      description: 'Temperature of the item'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WeatherObserved'    
      enum:    
        - WeatherObserved    
      type: Property    
    uVIndexMax:    
      description: 'The maximum UV index for the period, based on the World Health Organization''s UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
    - dateObserved    
    - location    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de la NGSI V2 observados por el clima  
Aquí hay un ejemplo de un WeatherObserved en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
  "illuminance": 1000,  
  "refDevice": "device-0A3478",  
  "streamGauge": 50,  
  "snowHeight": 20,   
  "uvIndexMax": 1.0  
}  
```  
#### Ejemplo normalizado de WeatherObserved NGSI V2  
Aquí hay un ejemplo de un WeatherObserved en formato JSON como normalizado. Este es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
  },  
  "uvIndexMax": {  
    "value": 1.0  
  }  
}  
```  
#### Ejemplo de valores clave NGSI-LD observados por el clima  
Aquí hay un ejemplo de un WeatherObserved en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
    "type": "WeatherObserved",  
    "dateObserved": "2016-11-30T07:00:00.00Z",  
    "illuminance": 1000,  
    "temperature": 3.3,  
    "precipitation": 0,  
    "atmosphericPressure":938.9,  
    "pressureTendency": 0.5,  
    "refDevice":"urn:ngsi-ld:Device:device-0A3478",  
    "source": "http://www.aemet.es",  
    "windSpeed": 2,  
    "location": {  
      "type": "Point",  
      "coordinates": [-4.754444444,41.640833333]  
    },  
    "stationName": "Valladolid",  
    "address":{  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES"  
    },  
    "stationCode": "2422",  
    "dataProvider": "TEF",  
    "windDirection": -45,  
    "relativeHumidity": 1,  
    "streamGauge":50,  
    "snowHeight": 20,  
    "uvIndexMax":1.0,  
    "@context": ["https://smart-data-models.github.io/data-models/context.jsonld"]  
}  
```  
#### Ejemplo normalizado de la NGSI-LD WeatherObserved  
Aquí hay un ejemplo de un WeatherObserved en formato JSON-LD como normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
            "coordinates": [  
                -4.754444444,  
                41.640833333  
            ]  
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
    "uvIndexMax": {  
        "type": "Property",  
        "value": 1.0  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
