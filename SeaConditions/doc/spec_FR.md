<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SeaConditions  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Weather/blob/master/SeaConditions/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description géographique harmonisée des conditions de mer**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved[string]`: La date et l'heure de cette observation au format ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Une description de cet article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pH[number]`: Acidité ou basicité d'une solution aqueuse.  . Model: [https://schema.org/Number](https://schema.org/Number)- `salinity[number]`: Quantité de sels dissous dans l'eau.  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `surfaceTemperature[number]`: Température de surface de la mer.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type d'entité NGSI-LD. Il doit s'agir de SeaConditions  - `waveHeight[number]`: Hauteur des vagues.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waveLevel[number]`: Il indique la hauteur des vagues et mesure également la houle de la mer.  . Model: [https://schema.org/Number](https://schema.org/Number)- `wavePeriod[number]`: Indique le temps entre les crêtes d'une vague.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SeaConditions:    
  description: 'This entity contains a harmonised geographic description of sea conditions'    
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
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &seaconditions_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *seaconditions_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pH:    
      description: 'Acidity or basicity of an aqueous solution.'    
      maximum: 14    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    salinity:    
      description: 'Amount of salts dissolved in water.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Parts per thousand'    
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
    surfaceTemperature:    
      description: 'Sea surface temperature.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Celsius degrees'    
    type:    
      description: 'NGSI-LD Entity Type. It has to be SeaConditions'    
      enum:    
        - SeaConditions    
      type: string    
      x-ngsi:    
        type: Property    
    waveHeight:    
      description: 'Height of the waves.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Meters    
    waveLevel:    
      description: 'It indicates the height of the waves and also measures the swell of the sea.'    
      maximum: 9    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Douglas sea scale'    
    wavePeriod:    
      description: 'Indicates the time between the crests of a wave.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Seconds    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/SeaConditions/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/SeaConditions/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### SeaConditions NGSI-v2 key-values Exemple  
Voici un exemple de SeaConditions au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "SeaCondition-PlayaLevante-Benidorm-123456",  
  "type": "SeaConditions",  
  "dateObserved": "2021-02-20T06:45:00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ]  
  },  
  "name": "Mar en la Playa Levante",  
  "description": "Información del estado del mar en la playa Levante",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Benidorm"  
  },  
  "dataProvider": "Water-sensor-12345",  
  "waveLevel": 1,  
  "surfaceTemperature": 14.7,  
  "waveHeight": 0.05,  
  "wavePeriod": 1.5,  
  "pH": 8.5,  
  "salinity": 35  
}  
```  
</details>  
#### SeaConditions NGSI-v2 normalisé Exemple  
Voici un exemple de SeaConditions au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "SeaCondition-PlayaLevante.Benidorm.123456",  
  "type": "SeaConditions",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2021-02-20T06:45:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value":  "2021-02-20T06:45:00Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Mar en la Playa Levante"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Playa Levante"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Información del estado del mar en la playa Levante"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Water-sensor-12345"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SeaConditions:items:JVPZ:12516420",  
      "urn:ngsi-ld:SeaConditions:items:XVAE:29040891"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SeaConditions:items:KFKA:73977455",  
      "urn:ngsi-ld:SeaConditions:items:GPZI:53207694"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "",  
      "addressLocality": "Benidorm",  
      "addressRegion": "Valencia",  
      "addressCountry": "ES",  
      "postalCode": "",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "waveLevel": {  
    "type": "Number",  
    "value": 1  
  },  
  "surfaceTemperature": {  
    "type": "Number",  
    "value": 14.7  
  },  
  "waveHeight": {  
    "type": "Number",  
    "value": 0.05  
  },  
  "wavePeriod": {  
    "type": "Number",  
    "value": 1.5  
  },  
  "pH": {  
    "type": "Number",  
    "value": 8.5  
  },  
  "salinity": {  
    "type": "Number",  
    "value": 35  
  },  
  "dateObserved": {  
    "type": "Number",  
    "value": "2021-02-20T06:45:00Z"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### Conditions de la mer Valeurs-clés NGSI-LD Exemple  
Voici un exemple de SeaConditions au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SeaCondition:SeaCondition-PlayaLevante-Benidorm-123456",  
    "type": "SeaConditions",  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Benidorm"  
    },  
    "dataProvider": "Water-sensor-12345",  
    "dateObserved": "2021-02-20T06:45:00Z",  
    "description": "Informaci\u00f3n del estado del mar en la playa Levante",  
    "location": {  
        "coordinates": [  
            -8.768460000000001,  
            42.60214472222222  
        ],  
        "type": "Point"  
    },  
    "name": "Mar en la Playa Levante",  
    "pH": 8.5,  
    "salinity": 35,  
    "surfaceTemperature": 14.7,  
    "waveHeight": 0.05,  
    "waveLevel": 1,  
    "wavePeriod": 1.5,  
    "@context": [  
        "https://smaertdatamodels.org/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Conditions de la mer NGSI-LD normalisé Exemple  
Voici un exemple de SeaConditions au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SeaCondition:SeaCondition-PlayaLevante-Benidorm-123456",  
    "type": "SeaConditions",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "",  
            "addressLocality": "Benidorm",  
            "addressRegion": "Valencia",  
            "addressCountry": "ES",  
            "postalCode": "",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Playa Levante"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "Water-sensor-12345"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-02-20T06:45:00Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-02-20T06:45:00Z"  
        }  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2021-02-20T06:45:00Z"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Informaci\u00f3n del estado del mar en la playa Levante"  
    },  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -8.768460000000001,  
                42.60214472222222  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Mar en la Playa Levante"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:SeaConditions:items:JVPZ:12516420",  
            "urn:ngsi-ld:SeaConditions:items:XVAE:29040891"  
        ]  
    },  
    "pH": {  
        "type": "Property",  
        "value": 8.5  
    },  
    "salinity": {  
        "type": "Property",  
        "value": 35  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:SeaConditions:items:KFKA:73977455",  
            "urn:ngsi-ld:SeaConditions:items:GPZI:53207694"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "surfaceTemperature": {  
        "type": "Property",  
        "value": 14.7  
    },  
    "waveHeight": {  
        "type": "Property",  
        "value": 0.05  
    },  
    "waveLevel": {  
        "type": "Property",  
        "value": 1  
    },  
    "wavePeriod": {  
        "type": "Property",  
        "value": 1.5  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
