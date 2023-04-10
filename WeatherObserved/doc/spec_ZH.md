<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：天气观测  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**对某一地点和时间的天气状况的观察。这个数据模型是与移动运营商和GSMA合作开发的**。  
版本：0.3.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `airQualityIndex[number]`: 空气质量指数是一个用于报告任何一天的空气质量的数字。  . Model: [https://schema.org/Number](https://schema.org/Number)- `airQualityIndexForecast[number]`: 预测未来一定时间内的整体空气质量指数（AQI）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureForecast[number]`: 未来一定时间内空气温度的预测值。  . Model: [https://schema.org/Number](https://schema.org/Number)- `airTemperatureTSA[object]`: 定义一个基本属性在一个时期内的时间处理的对象。它提供了最大值、最小值、即时值和平均值。  - `alternateName[string]`: 这个项目的一个替代名称  - `aqiMajorPollutant[string]`: 空气质量指数（AQI）中的主要污染物。  . Model: [https://schema.org/Text](https://schema.org/Text)- `aqiMajorPollutantForecast[string]`: 预测未来一定时间内空气质量指数（AQI）中的主要空气污染物。  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: 观察到的大气压力以Hecto Pascals为单位。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 由用户定义的被观察实体的日期。  - `description[string]`: 对这个项目的描述  - `dewPoint[number]`: 编码为数字的露点。观察到的温度，空气必须冷却到这个温度才会有饱和的水蒸气。  . Model: [https://schema.org/Number](https://schema.org/Number)- `feelLikesTemperature[number]`: 项目的温度欣赏  - `gustSpeed[number]`: 突然爆发的高速风，超过观察到的平均风速，只持续了几秒钟。  - `id[*]`: 实体的唯一标识符  - `illuminance[number]`: 观察到的瞬时环境光强度  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `precipitation[number]`: 登记的水雨量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `precipitationForecast[number]`: 预测未来一定时间内的降雨量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressureTendency[*]`: Enum:'下降、上升、稳定'。压力是上升还是下降？可以用定量的术语或定性的术语来表达。  - `refDevice[*]`: 捕获该观察结果的设备的参考。  . Model: [https://schema.org/URL](https://schema.org/URL)- `refPointOfInterest[string]`: 与该项目有关的兴趣点  . Model: [http://schema.org/URL](http://schema.org/URL)- `relativeHumidity[number]`: 空气中的湿度。观测到的瞬时相对湿度（空气中的水蒸气）。  - `relativeHumidityForecast[number]`: 预测未来一定时间内的相对湿度（空气中的水蒸气）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `snowHeight[number]`: 通用雪深测量传感器观测到的雪高，用厘米表示  . Model: [https://schema.org/Number](https://schema.org/Number)- `solarRadiation[number]`: 观察到的太阳辐射以每平方瓦特为单位。  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `streamGauge[number]`: 水文测量传感器观察到的水面高程，即以厘米为单位的[水流测量仪](https://en.wikipedia.org/wiki/Stream_gauge)。  . Model: [https://schema.org/Number](https://schema.org/Number)- `temperature[number]`: 项目的温度  - `type[string]`: NGSI实体类型。它必须是WeatherObserved  - `uVIndexMax[number]`: 根据世界卫生组织的紫外线指数测量，该时期的最大紫外线指数。[http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)1到11之间的数值是该指数的有效范围。值0是用于描述没有检测到信号，所以不存储任何值。  . Model: [https://schema.org/Number](https://schema.org/Number)- `visibility[*]`: 能见度的类别  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: 天气的文字描述  . Model: [http://schema.org/Text.](http://schema.org/Text.)- `windDirection[number]`: 赌风的方向  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: 风的强度  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
根据[世界气象组织]定义的风向范围(https://library.wmo.int/doc_num.php?explnum_id=3177)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    airQualityIndex:    
      description: Air quality index is a number used to report the quality of the air on any given day.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airQualityIndexForecast:    
      description: Forecasted overall Air Quality Index (AQI) over a certain duration in future.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airTemperatureForecast:    
      description: Forecasted value of air temperature over a certain duration in future.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    airTemperatureTSA:    
      description: 'Object defining the temporal processing of a basic property during a period. It provides Maximum, minimum, instant value and average'    
      properties:    
        averageValue:    
          type: number    
        instValue:    
          type: number    
        maxOverTime:    
          type: number    
        minOverTime:    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    aqiMajorPollutant:    
      description: Major pollutant in the Air Quality Index (AQI).    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    aqiMajorPollutantForecast:    
      description: Forecasted major air pollutant in the Air Quality Index (AQI) over a certain duration in future.    
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
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: Date of the observed entity defined by the user.    
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
    feelLikesTemperature:    
      description: Temperature appreciation of the item    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &weatherobserved_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
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
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *weatherobserved_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
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
      description: Forecasted rainfall over a certain duration in future.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pressureTendency:    
      description: 'Enum:''falling, raising, steady''. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms.'    
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
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: A reference to the device(s) which captured this observation.    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'The maximum UV index for the period, based on the World Health Organization''s UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) the values between 1 and 11 are the valid range for the index. The value 0 is for describing that no signal is detected so no value is stored.'    
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
        model: http://schema.org/Text.    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherObserved/schema.json    
  x-model-tags: IUDX    
  x-version: 0.3.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### WeatherObserved NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的WeatherObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### WeatherObserved NGSI-v2 normalized Example  
下面是一个以JSON-LD格式规范化的WeatherObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### WeatherObserved NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的WeatherObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### WeatherObserved NGSI-LD 归一化实例  
这里是一个以JSON-LD格式规范化的WeatherObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
    "type": "WeatherObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Valladolid",  
            "addressCountry": "ES",  
            "type": "PostalAddress"  
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
        "https://smart-data-models.github.io/dataModel.Weather/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
