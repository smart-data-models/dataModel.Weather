from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AirTemperatureTSA(BaseModel):
    averageValue: Optional[float] = Field(
        None, description='Average value of temporal processing over time'
    )
    instValue: Optional[float] = Field(
        None, description='Instant value of temporal processing'
    )
    maxOverTime: Optional[float] = Field(
        None, description='Maximum value of temporal processing over time'
    )
    minOverTime: Optional[float] = Field(
        None, description='Minimum value of temporal processing over time'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class PressureTendency(Enum):
    falling = 'falling'
    raising = 'raising'
    steady = 'steady'


class Type6(Enum):
    WeatherObserved = 'WeatherObserved'


class Visibility(Enum):
    veryPoor = 'veryPoor'
    poor = 'poor'
    moderate = 'moderate'
    good = 'good'
    veryGood = 'veryGood'
    excellent = 'excellent'


class WeatherObserved(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    airQualityIndex: Optional[float] = Field(
        None,
        description='Air quality index is a number used to report the quality of the air on any given day',
    )
    airQualityIndexForecast: Optional[float] = Field(
        None,
        description='Forecasted overall Air Quality Index (AQI) over a certain duration in future',
    )
    airTemperatureForecast: Optional[float] = Field(
        None,
        description='Forecasted value of air temperature over a certain duration in future',
    )
    airTemperatureTSA: Optional[AirTemperatureTSA] = Field(
        None, description='Air temperature time series aggregation'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    aqiMajorPollutant: Optional[str] = Field(
        None, description='Major pollutant in the Air Quality Index (AQI)'
    )
    aqiMajorPollutantForecast: Optional[str] = Field(
        None,
        description='Forecasted major air pollutant in the Air Quality Index (AQI) over a certain duration in future',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    atmosphericPressure: Optional[confloat(ge=0.0)] = Field(
        None, description='The atmospheric pressure observed measured in Hecto Pascals'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateObserved: Optional[AwareDatetime] = Field(
        None, description='Date of the observed entity defined by the user'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dewPoint: Optional[float] = Field(
        None,
        description='The dew point encoded as a number. Observed temperature to which air must be cooled to become saturated with water vapor',
    )
    diffuseIrradiation: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Diffuse irradiance is the part of the solar irradiance that is scattered by the atmosphere',
    )
    directIrradiation: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Direct irradiance is the part of the solar irradiance that directly reaches a surface',
    )
    feelsLikeTemperature: Optional[float] = Field(
        None, description='Temperature appreciation of the item'
    )
    gustSpeed: Optional[float] = Field(
        None,
        description='A sudden burst of high-speed wind over the observed average wind speed lasting only for a few seconds',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    illuminance: Optional[confloat(ge=0.0)] = Field(
        None,
        description='(https://en.wikipedia.org/wiki/Illuminance) observed measured in lux (lx) or lumens per square metre (cd·sr·m−2)',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    precipitation: Optional[confloat(ge=0.0)] = Field(
        None, description='Amount of water rain registered. '
    )
    precipitationForecast: Optional[float] = Field(
        None, description='Forecasted rainfall over a certain duration in future'
    )
    pressureTendency: Optional[Union[PressureTendency, float]] = Field(
        None,
        description="Enum:'falling, raising, steady'. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms",
    )
    refDevice: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='A reference to the device(s) which captured this observation'
    )
    refPointOfInterest: Optional[str] = Field(
        None, description='Point of interest related to the item'
    )
    relativeHumidity: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)',
    )
    relativeHumidityForecast: Optional[float] = Field(
        None,
        description='Forecasted relative humidity (water vapour in air) over a certain duration in future',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    snowHeight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The snow height observed by generic snow depth measurement sensors, expressed in centimeters',
    )
    solarRadiation: Optional[confloat(ge=0.0)] = Field(
        None, description='The solar radiation observed measured in Watts per square'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    streamGauge: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The water level surface elevation observed by Hydrometric measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expressed in centimeters',
    )
    temperature: Optional[float] = Field(None, description='Temperature of the item')
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be WeatherObserved'
    )
    uVIndexMax: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The maximum UV index for the period, based on the World Health Organization's UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/) the values between 1 and 11 are the valid range for the index. The value 0 is for describing that no signal is detected so no value is stored",
    )
    visibility: Optional[Union[Visibility, confloat(ge=0.0)]] = Field(
        None, description='Categories of visibility'
    )
    weatherType: Optional[str] = Field(
        None, description='Text description of the weather'
    )
    windDirection: Optional[confloat(ge=0.0, le=360.0)] = Field(
        None, description='Direction of the wind bet'
    )
    windSpeed: Optional[confloat(ge=0.0)] = Field(
        None, description='Intensity of the wind'
    )
