<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体天气观测    
======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**对某一地点和时间的天气状况的观测。该数据模型是与移动运营商和 GSMA 合作开发的。    
版本： 0.3.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `airQualityIndex[number]`: 空气质量指数是用来报告任何一天的空气质量的数字  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityIndexForecast[number]`: 未来一定时间内的总体空气质量指数（AQI）预测值  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureForecast[number]`: 未来一定时间内的气温预测值  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureTSA[object]`: 气温时间序列汇总  	- `averageValue[number]`: 随时间变化的时间处理平均值      
	- `instValue[number]`: 时间处理的即时价值      
	- `maxOverTime[number]`: 时间处理的最大值      
- `alternateName[string]`: 该项目的替代名称  - `aqiMajorPollutant[string]`: 空气质量指数（AQI）中的主要污染物  . Model: [https://schema.org/Text](https://schema.org/Text)- `aqiMajorPollutantForecast[string]`: 未来一定时间内空气质量指数（AQI）中主要空气污染物的预测值  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[date-time]`: 用户定义的被观测实体的日期  - `description[string]`: 项目描述  - `dewPoint[number]`: 以数字编码的露点。空气必须冷却到什么温度才能达到水蒸气饱和的观测温度  . Model: [https://schema.org/Number](https://schema.org/Number)- `diffuseIrradiation[number]`: 漫射辐照度是太阳辐照度中被大气散射的部分  . Model: [https://schema.org/Number](https://schema.org/Number)- `directIrradiation[number]`: 直接辐照度是太阳辐照度中直接到达表面的部分  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `illuminance[number]`: 观测到的瞬时环境光强  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一标识  - `precipitation[number]`: 登记的雨水量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationForecast[number]`: 未来某段时间的降雨量预测  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressureTendency[*]`: 枚举："下降、升高、稳定"。压力是上升还是下降？可以用定量或定性来表示  - `refDevice[*]`: 捕捉这一观测结果的设备的参考信息  . Model: [https://schema.org/URL](https://schema.org/URL)- `relativeHumidity[number]`: 空气湿度。观测到的瞬时相对湿度（空气中的水蒸气）  - `relativeHumidityForecast[number]`: 未来一定时间内的相对湿度（空气中的水蒸气）预测值  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `snowHeight[number]`: 通用雪深测量传感器观测到的雪高，以厘米为单位  . Model: [https://schema.org/Number](https://schema.org/Number)- `solarRadiation[number]`: 观测到的太阳辐射以瓦特每平方  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `streamGauge[number]`: 水文测量传感器（即[测流仪](https://en.wikipedia.org/wiki/Stream_gauge)）观测到的水位面高程，单位为厘米  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: 物品的温度  - `type[string]`: NGSI 实体类型。必须是 WeatherObserved  - `uVIndexMax[number]`: 根据世界卫生组织的紫外线指数衡量标准，该时段的最大紫外线指数。[http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)1 到 11 之间的数值是该指数的有效范围。数值 0 表示没有检测到信号，因此不存储数值。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
根据[世界气象组织](https://library.wmo.int/doc_num.php?explnum_id=3177) 确定的风向范围    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### WeatherObserved NGSI-v2 关键值示例    
下面是一个以 JSON-LD 格式作为键值的 WeatherObserved 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### WeatherObserved NGSI-v2 normalized 示例    
下面是一个规范化的 JSON-LD 格式 WeatherObserved 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
    "type": "Boolean",  
    "value": false  
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
  "stationName": {  
    "type": "Text",  
    "value": "Valladolid"  
  },  
  "address": {  
    "type": "StructuredValue",  
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
    "type": "Boolean",  
    "value": true  
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
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### WeatherObserved NGSI-LD key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 WeatherObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### 天气观测 NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 WeatherObserved 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
