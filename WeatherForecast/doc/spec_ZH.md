<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。天气预报  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherForecast/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**对天气预报的统一描述**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atmosphericPressure[number]`: 观察到的大气压力以Hecto Pascals为单位。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateIssued[string]`: 气象局发布预报的日期和时间，格式为ISO8601 UTC。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateRetrieved[string]`: 以ISO8601 UTC格式检索预报的日期和时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dayMaximum[object]`: 报告期间的最高值。子属性：- `temperature`：最高温度。描述和单位见`WeatherForecast.temperature'。- `感觉温度'。最大的感觉温度。与`WeatherForecast.feelLikeTemperature'的语义和单位相同。最大的相对湿度。与`WeatherForecast.relativeHumidity'的语义和单位相同。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dayMinimum[object]`: 报告期内预测的最低值。  报告期间的最低值。子属性：- `temperature`：最低温度。描述和单位见`WeatherForecast.temperature'。- `感觉温度'。最低感觉温度。与`WeatherForecast.feelLikeTemperature'的语义和单位相同。最低相对湿度。与`WeatherForecast.relativeHumidity`的语义和单位相同。  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: 对这个项目的描述  - `feelLikesTemperature[number]`: 项目的温度欣赏  - `gustSpeed[number]`: 突然爆发的高速风，超过观察到的平均风速，只持续了几秒钟。  - `id[*]`: 实体的唯一标识符  - `illuminance[number]`: (https://en.wikipedia.org/wiki/Illuminance)观察，以勒克斯(lx)或每平方米流明(cd-sr-m-2)衡量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `precipitation[number]`: 预计的水雨量  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPointOfInterest[string]`: 与该项目有关的兴趣点  . Model: [http://schema.org/URL](http://schema.org/URL)- `relativeHumidity[number]`: 空气中的湿度。观测到的瞬时相对湿度（空气中的水蒸气）。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `temperature[number]`: 项目的温度  - `type[string]`: NGSI实体类型。它必须是WeatherForecast  - `uVIndexMax[number]`: 根据世界卫生组织的紫外线指数测量，该时期的最大紫外线指数。规范性参考资料。[http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)  . Model: [https://schema.org/Number](https://schema.org/Number)- `validFrom[string]`: 有效期的开始日期和时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `validTo[string]`: 有效期结束日期和时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `validity[string]`: 包括作为ISO8601时间间隔的该预测的有效期。作为Orion Context Broker不支持日期时间间隔的变通方法，它可以使用两个单独的属性。`validFrom`, `validTo`.  . Model: [https://schema.org/Text](https://schema.org/Text)- `visibility[*]`: 能见度的类别  . Model: [http://schema.org/Text](http://schema.org/Text)- `weatherType[string]`: 天气的文字描述  . Model: [http://schema.org/Text.](http://schema.org/Text.)- `windDirection[number]`: 赌风的方向  . Model: [http://schema.org/Number](http://schema.org/Number)- `windSpeed[number]`: 风的强度  . Model: [http//schema.org/Number](http//schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `address`  - `dateIssued`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
该实体主要与环境和农业的垂直领域相关，但也适用于许多不同的应用。这个数据模型是与移动运营商和[GSMA]（https://www.gsma.com/iot/iot-big-data/）合作开发的。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherForecast:    
  description: 'A harmonised description of a Weather Forecast'    
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
    atmosphericPressure:    
      description: 'The atmospheric pressure observed measured in Hecto Pascals'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Hecto pascals'    
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
    dateIssued:    
      description: 'The date and time the forecast was issued by the meteorological bureau in ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateRetrieved:    
      description: 'The date and time the forecast was retrieved in ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dayMaximum:    
      description: 'Maximum values for the reported period. Subattributes:- `temperature` : Maximum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Maximum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.-   `relativeHumidity`. Maximum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`.'    
      properties:    
        feelLikesTemperature:    
          description: 'Property. Temperature appreciation of the item'    
          type: number    
        relativeHumidity:    
          description: 'Property. Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
          maximum: 1    
          minimum: 0    
          type: number    
        temperature:    
          description: 'Property. Temperature of the item'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dayMinimum:    
      description: 'Minimum values forecasted for the reported period.  Minimum values for the reported period. Subattributes:- `temperature` : Minimum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Minimum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Minimum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`'    
      properties:    
        feelLikesTemperature:    
          description: 'Property. Temperature appreciation of the item'    
          type: number    
        relativeHumidity:    
          description: 'Property. Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
          maximum: 1    
          minimum: 0    
          type: number    
        temperature:    
          description: 'Property. Temperature of the item'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    feelLikesTemperature:    
      description: 'Temperature appreciation of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    gustSpeed:    
      description: 'A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds.'    
      type: number    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    illuminance:    
      description: '(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        anyOf: *weatherforecast_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    precipitation:    
      description: 'Amount of water rain expected'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Liters per square meter.'    
    refPointOfInterest:    
      description: 'Point of interest related to the item'    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    relativeHumidity:    
      description: 'Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
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
    temperature:    
      description: 'Temperature of the item'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WeatherForecast'    
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
      description: 'Validity period start date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    validTo:    
      description: 'Validity period end date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `validFrom`, `validTo`.'    
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
      description: 'Categories of visibility'    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    weatherType:    
      description: 'Text description of the weather'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text.    
        type: Property    
    windDirection:    
      description: 'Direction of the wind bet'    
      maximum: 180    
      minimum: -180    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    windSpeed:    
      description: 'Intensity of the wind'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - dateIssued    
    - address    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherForecast/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Weather/WeatherForecast/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### WeatherForecast NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的WeatherForecast的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### WeatherForecast NGSI-v2归一化实例  
下面是一个以JSON-LD格式规范化的WeatherForecast的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
    "value": 0  
  },  
  "validity": {  
    "type": "Text",  
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
    "type": "Number",  
    "value": 0.85  
  },  
  "uVIndexMax": {  
    "type": "Number",  
    "value": 1.00  
  }  
}  
```  
</details>  
#### WeatherForecast NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的WeatherForecast的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WeatherForecast:Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
    "type": "WeatherForecast",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "Spain",  
            "postalCode": "46005",  
            "addressLocality": "Valencia",  
            "type": "PostalAddress"  
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
    "uvIndexMax": {  
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
        "value": 0  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### WeatherForecast NGSI-LD 归一化实例  
下面是一个JSON-LD格式的规范化的WeatherForecast的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "Spain-WeatherForecast-46005_2016-12-01T18:00:00_2016-12-02T00:00:00",  
    "type": "WeatherForecast",  
    "address": {  
        "type": "PostalAddress",  
        "value": {  
            "addressCountry": "Spain",  
            "postalCode": "46005",  
            "addressLocality": "Valencia"  
        }  
    },  
    "dataProvider": {  
        "type": "Text",  
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
        "type": "Text",  
        "value": "overcast"  
    },  
    "windSpeed": {  
        "type": "Property",  
        "value": 0  
    },  
    "@context": [  
        "https://smartdatamdels.org/context.jsonld",  
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
