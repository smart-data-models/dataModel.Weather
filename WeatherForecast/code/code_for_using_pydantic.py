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


class DayMaximum(BaseModel):
    feelLikesTemperature: Optional[float] = Field(
        None, description='Temperature appreciation of the item'
    )
    relativeHumidity: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)',
    )
    temperature: Optional[float] = Field(None, description='Temperature of the item')


class DayMinimum(BaseModel):
    feelLikesTemperature: Optional[float] = Field(
        None, description='Temperature appreciation of the item'
    )
    relativeHumidity: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)',
    )
    temperature: Optional[float] = Field(None, description='Temperature of the item')


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


class Type6(Enum):
    WeatherForecast = 'WeatherForecast'


class Visibility(Enum):
    veryPoor = 'veryPoor'
    poor = 'poor'
    moderate = 'moderate'
    good = 'good'
    veryGood = 'veryGood'
    excellent = 'excellent'


class WeatherForecast(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
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
    dateIssued: Optional[AwareDatetime] = Field(
        None,
        description='The date and time the forecast was issued by the meteorological bureau in ISO8601 UTC format',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateRetrieved: Optional[AwareDatetime] = Field(
        None,
        description='The date and time the forecast was retrieved in ISO8601 UTC format',
    )
    dayMaximum: Optional[DayMaximum] = Field(
        None,
        description='Maximum values for the reported period. Subattributes:- `temperature` : Maximum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Maximum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.-   `relativeHumidity`. Maximum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`',
    )
    dayMinimum: Optional[DayMinimum] = Field(
        None,
        description='Minimum values forecasted for the reported period.  Minimum values for the reported period. Subattributes:- `temperature` : Minimum temperature. See `WeatherForecast.temperature` for description and units. - `feelLikesTemperature`. Minimum feels like temperature. Same semantics and units as `WeatherForecast.feelsLikeTemperature`.- `relativeHumidity`. Minimum relative humidity. Same semantics and units as `WeatherForecast.relativeHumidity`',
    )
    description: Optional[str] = Field(None, description='A description of this item')
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
        None, description='Amount of water rain expected'
    )
    precipitationProbability: Optional[confloat(ge=0.0)] = Field(
        None, description='Probability of rainfall.'
    )
    refPointOfInterest: Optional[str] = Field(
        None, description='Point of interest related to the item'
    )
    relativeHumidity: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Humidity in the Air. Observed instantaneous relative humidity (water vapour in air)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    temperature: Optional[float] = Field(None, description='Temperature of the item')
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be WeatherForecast'
    )
    uVIndexMax: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The maximum UV index for the period, based on the World Health Organization's UV Index measure. Normative references: [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)",
    )
    validFrom: Optional[AwareDatetime] = Field(
        None, description='Validity period start date and time'
    )
    validTo: Optional[AwareDatetime] = Field(
        None, description='Validity period end date and time'
    )
    validity: Optional[str] = Field(
        None,
        description='Includes the validity period for this forecast as a ISO8601 time interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `validFrom`, `validTo`',
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
