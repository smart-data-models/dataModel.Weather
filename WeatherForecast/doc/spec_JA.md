<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティウェザーフォーキャスト  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherForecast/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**天気予報の調和された記述。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: 大気圧の単位はヘクトパスカル。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateIssued[date-time]`: 予報が気象局によって発表された日時。ISO8601 UTCフォーマット。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateRetrieved[date-time]`: 予報が取得された日付と時刻。ISO8601 UTCフォーマット。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dayMaximum[object]`: 報告された期間の最大値。Subattributes:- `temperature` : 最高気温。説明と単位は `WeatherForecast.temperature` を参照。- feelLikesTemperature`.体感温度の最大値。意味と単位は `WeatherForecast.feelLikeTemperature`と同じ。相対湿度の最大値。WeatherForecast.relativeHumidity`と同じ意味・単位。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `feelLikesTemperature[number]`: アイテムの温度評価    
	- `relativeHumidity[number]`: 空気中の湿度。観測された瞬間相対湿度（空気中の水蒸気）    
	- `temperature[number]`: 商品の温度    
- `dayMinimum[object]`: 報告された期間の最低予測値。  報告された期間の最小値。Subattributes:- `temperature` : 最低気温。説明と単位は `WeatherForecast.temperature` を参照。- feelLikesTemperature`.最低気温。意味と単位は `WeatherForecast.feelLikeTemperature`と同じ。相対湿度の最小値。WeatherForecast.relativeHumidity`と同じ意味・単位。  . Model: [https://schema.org/Text](https://schema.org/Text)	- `feelLikesTemperature[number]`: アイテムの温度評価    
	- `relativeHumidity[number]`: 空気中の湿度。観測された瞬間相対湿度（空気中の水蒸気）    
	- `temperature[number]`: 商品の温度    
- `description[string]`: この商品の説明  - `feelLikesTemperature[number]`: アイテムの温度評価  - `gustSpeed[number]`: 観測された平均風速を超える高速の風が数秒間だけ突然吹き荒れること。  - `id[*]`: エンティティの一意識別子  - `illuminance[number]`: (https://en.wikipedia.org/wiki/Illuminance) ルクス（lx）またはルーメン/平方メートル（cd-sr-m-2）で測定される。  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `precipitation[number]`: 予想される雨量  . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationProbability[number]`: 降水確率。  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPointOfInterest[string]`: アイテムに関連するポイント  . Model: [http://schema.org/URL](http://schema.org/URL)- `relativeHumidity[number]`: 空気中の湿度。観測された瞬間相対湿度（空気中の水蒸気）  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `temperature[number]`: 商品の温度  - `type[string]`: NGSI エンティティタイプ。WeatherForecastでなければならない。  - `uVIndexMax[number]`: 世界保健機関（WHO）のUVインデックスに基づく、その期間の最大UVインデックス。標準的な参考文献：[http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  . Model: [https://schema.org/Number](https://schema.org/Number)- `validFrom[date-time]`: 有効期間開始日時  . Model: [https://schema.org/Text](https://schema.org/Text)- `validTo[date-time]`: 有効期間終了日時  . Model: [https://schema.org/Text](https://schema.org/Text)- `validity[string]`: この予測の有効期間をISO8601時間間隔として含む。Orion Context Broker が日付間隔をサポートしていない場合の回避策として、2 つの別々の属性を使用することができます：validFrom`、`validTo`。  . Model: [https://schema.org/Text](https://schema.org/Text)- `visibility[*]`: 視認性のカテゴリー  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: 天気のテキスト説明  . Model: [http://schema.org/Text](http://schema.org/Text)- `windDirection[number]`: 風向き  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: 風の強さ  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `dateIssued`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このエンティティは主に環境と農業の垂直セグメントに関連しているが、多くの異なるアプリケーションに適用可能である。このデータ・モデルは、移動体通信事業者および[GSMA](https://www.gsma.com/iot/iot-big-data/)と協力して開発された。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
      description: Amount of water rain expected    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter    
    precipitationProbability:    
      description: Probability of rainfall.    
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
    relativeHumidity:    
      description: Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: Temperature of the item    
      type: number    
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
    - dateIssued    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherForecast/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### WeatherForecast NGSI-v2 キー値の例  
以下は、JSON-LD形式のWeatherForecastのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### WeatherForecast NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のWeatherForecastの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": 0.2  
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
    "type": "Number",  
    "value": 1.0  
  }  
}  
```  
</details>  
#### WeatherForecast NGSI-LD キー値の例  
以下は、JSON-LD形式のWeatherForecastをkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### WeatherForecast NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の WeatherForecast の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": 0.2  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
