<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ天気観測  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
世界的な記述：**ある場所と時間における気象状況の観測。このデータモデルは、携帯電話会社とGSMAの協力により開発された**。  
バージョン: 0.3.2  
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
- `airQualityIndex[number]`: 大気の質指数とは、その日の大気の質を表す数値。  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityIndexForecast[number]`: 将来の一定期間の総合大気質指数（AQI）予測  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureForecast[number]`: 将来の一定期間の気温の予測値  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureTSA[object]`: 気温時系列集計  	- `averageValue[number]`: 時間的処理の経時的平均値    
	- `instValue[number]`: 時間的処理の瞬間的価値    
	- `maxOverTime[number]`: 時間的処理の最大値    
- `alternateName[string]`: この項目の別名  - `aqiMajorPollutant[string]`: 大気質指標（AQI）の主要汚染物質  . Model: [https://schema.org/Text](https://schema.org/Text)- `aqiMajorPollutantForecast[string]`: 将来の一定期間における大気質指標（AQI）における主要大気汚染物質の予測値。  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[date-time]`: ユーザーが定義した観測されたエンティティの日付  - `description[string]`: この商品の説明  - `dewPoint[number]`: 露点を数値で表したもの。空気が水蒸気で飽和状態になるために冷却しなければならない温度。  . Model: [https://schema.org/Number](https://schema.org/Number)- `diffuseIrradiation[number]`: 拡散放射照度とは、太陽放射照度のうち大気によって散乱される部分のことである。  . Model: [https://schema.org/Number](https://schema.org/Number)- `directIrradiation[number]`: 直接放射照度とは、太陽放射照度のうち、地表に直接到達する部分である。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `illuminance[number]`: 観測された瞬間周囲光強度  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `precipitation[number]`: 登録された雨の量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationForecast[number]`: 将来の一定期間の降雨量予測  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressureTendency[*]`: Enum:'下降、上昇、安定'.圧力は上昇しているのか、下降しているのか。それは量的な用語でも質的な用語でも表すことができる。  - `refDevice[*]`: この観測を捕らえた機器へのリファレンス。  . Model: [https://schema.org/URL](https://schema.org/URL)- `relativeHumidity[number]`: 空気中の湿度。観測された瞬間相対湿度（空気中の水蒸気）  - `relativeHumidityForecast[number]`: 将来の一定期間における相対湿度（空気中の水蒸気量）の予測値。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `snowHeight[number]`: 汎用の積雪深測定センサーで観測された雪の高さ。  . Model: [https://schema.org/Number](https://schema.org/Number)- `solarRadiation[number]`: 観測された日射量は、1平方あたりワットで測定された。  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `streamGauge[number]`: 水位計測センサー、すなわち[Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge)によって観測された水位面の高さをセンチメートル単位で表したもの。  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: 商品の温度  - `type[string]`: NGSI Entity タイプ。WeatherObserved でなければならない。  - `uVIndexMax[number]`: 世界保健機関（WHO）のUVインデックスに基づく、その期間の最大UVインデックス。[http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)1～11の値がインデックスの有効範囲です。値0は、信号が検出されなかったことを表すため、値は保存されません。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
世界気象機関](https://library.wmo.int/doc_num.php?explnum_id=3177)に従って定義された風向範囲。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### WeatherObserved NGSI-v2 キー値の例  
以下は、JSON-LD形式のWeatherObservedのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### WeatherObserved NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の WeatherObserved の例である。これは、オプションを使用しない場合、NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。  
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
#### WeatherObserved NGSI-LD キー値の例  
以下は、WeatherObserved を JSON-LD 形式で key-values とした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### WeatherObserved NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の WeatherObserved の例である。これは、オプションを使用しない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキスト・データを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
