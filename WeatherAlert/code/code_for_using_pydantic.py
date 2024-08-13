from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


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


class Category(Enum):
    traffic = 'traffic'
    naturalDisaster = 'naturalDisaster'
    weather = 'weather'
    environment = 'environment'
    health = 'health'
    security = 'security'
    agriculture = 'agriculture'


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


class Severity(Enum):
    informational = 'informational'
    low = 'low'
    medium = 'medium'
    high = 'high'
    critical = 'critical'


class SubCategory(Enum):
    avalanches = 'avalanches'
    coastalEvent = 'coastalEvent'
    coldWave = 'coldWave'
    flood = 'flood'
    fog = 'fog'
    forestFire = 'forestFire'
    heatWave = 'heatWave'
    highTemperature = 'highTemperature'
    hurricane = 'hurricane'
    ice = 'ice'
    lowTemperature = 'lowTemperature'
    rainfall = 'rainfall'
    rain_flood = 'rain_flood'
    snow = 'snow'
    snow_ice = 'snow_ice'
    thunderstorms = 'thunderstorms'
    tornado = 'tornado'
    tropicalCyclone = 'tropicalCyclone'
    tsunami = 'tsunami'
    wind = 'wind'


class Type6(Enum):
    WeatherAlert = 'WeatherAlert'


class WeatherAlert(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alertSource: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Source of the alert')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    category: Optional[Category] = Field(
        None,
        description="Category of the Alert. Enum:'traffic, naturalDisaster, weather, environment, health, security, agriculture'",
    )
    data: Optional[Dict[str, Any]] = Field(
        None, description='Payload containing the data retrieved'
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
        None, description='The date and time the item was issued in ISO8601 UTC format'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    severity: Optional[Severity] = Field(None, description='Severity of the Alarm')
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    subCategory: Optional[SubCategory] = Field(
        None,
        description="Weather categories. Enum:' avalanches,coastalEvent, coldWave, flood, fog, forestFire, heatWave, highTemperature, hurricane, ice, lowTemperature, rainfall, rain_flood, snow, snow_ice, thunderstorms, tornado, tropicalCyclone, tsunami, wind'",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be WeatherAlert'
    )
    validFrom: Optional[AwareDatetime] = Field(
        None,
        description='The start of the validity period for this forecast as a ISO8601 format',
    )
    validTo: Optional[AwareDatetime] = Field(
        None,
        description='The end of the validity period for this forecast as a ISO8601 format',
    )
