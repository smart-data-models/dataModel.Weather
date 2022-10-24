<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティシーコンディショニング  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Weather/blob/master/SeaConditions/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**このエンティティは、海況の調和された地理的記述を含む**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[string]`: ISO8601 UTC フォーマットでのこの観測の日付と時刻。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `pH[number]`: 水溶液の酸性度または塩基性度。  . Model: [https://schema.org/Number](https://schema.org/Number)- `salinity[number]`: 水に溶けている塩の量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `surfaceTemperature[number]`: 海面水温。  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-LDのエンティティタイプ。SeaConditionsでなければならない。  - `waveHeight[number]`: 波の高さ  . Model: [https://schema.org/Number](https://schema.org/Number)- `waveLevel[number]`: 波の高さを示すとともに、海のうねりを測ることができます。  . Model: [https://schema.org/Number](https://schema.org/Number)- `wavePeriod[number]`: 波の頂点と頂点の間の時間を示す。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### SeaConditions NGSI-v2 key-value の例。  
SeaConditionsをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### SeaConditions NGSI-v2 正規化例  
SeaConditions を JSON-LD 形式で正規化した例を示す。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### SeaConditions NGSI-LD key-value 例  
SeaConditionsをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### SeaConditions NGSI-LD 正規化例  
SeaConditions を JSON-LD 形式で正規化した例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
