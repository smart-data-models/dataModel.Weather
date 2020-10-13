# Weather Forecast

## Description

This entity contains a harmonised description of a Weather Forecast. This entity
is primarily associated with the vertical segments of the environment and
agriculture but is applicable to many different applications.

This data model has been developed in cooperation with mobile operators and the
[GSMA](https://www.gsma.com/iot/iot-big-data/).

You can see a description of weather forecast parameters provided by AEMET (in
Spanish) [here](http://www.aemet.es/es/eltiempo/prediccion/municipios/ayuda).

## Data Model

A JSON Schema corresponding to this data model can be found
[here](http://smart-data-models.github.io/dataModel.Weather/WeatherForecast/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `WeatherForecast`.

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.
-   `name` : Name given to the weather forecast location.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/name` equivalent to [name](https://schema.org/name)
    -   Optional

-   `location` : Location of the weather observation represented by a GeoJSON
    geometry.
    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `address` is not defined.
-   `address` : Civic address of the weather forecast.
    -   Normative References:
        [https://schema.org/address](https://schema.org/address)
    -   Mandatory if `location` is not present.
-   `dateRetrieved` : The date and time the forecast was retrieved in ISO8601
    UTC format.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime).
    -   Mandatory
-   `dateIssued` : The date and time the forecast was issued by the
    meteorological bureau in ISO8601 UTC format.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime).
    -   Mandatory
-   `validity` : Includes the validity period for this forecast as a ISO8601
    time interval. As a workaround for the lack of support of Orion Context
    Broker for datetime intervals, it can be used two separate attributes:
    `validFrom`, `validTo`.
    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Mandatory
-   `validFrom` : Validity period start date and time.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime).
    -   Optional
-   `validTo` : Validity period end date and time.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime).
    -   Optional
-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `refPointOfInterest` : A reference to a point of interest associated to this
    forecast.
    -   Attribute type: Relationship. Reference to an entity of type `PointOfInterest`
    -   Optional
-   `weatherType` : The forecasted weather type.
    -   See [WeatherObserved.weatherType](../WeatherObserved/README.md) for
        description and allowed values.
    -   Optional
-   `visibility` : Visibility forecasted.

    -   See [WeatherObserved.visibility](../WeatherObserved/README.md) for
        description and allowed values.
    -   Optional

-   `temperature` : Air's temperature forecasted.
    -   See [WeatherObserved.temperature](../WeatherObserved/README.md) for
        description and units.
    -   Optional
-   `feelsLikeTemperature` : Feels like temperature forecasted.

    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Default unit: Degrees centigrades.
    -   Optional

-   `relativeHumidity` : Air's relative humidity forecasted (percentage,
    expressed in parts per one).

    -   See
        [WeatherObserved.relativeHumidity](../WeatherObserved/README.md)
        for description and units.
    -   Optional

-   `precipitationProbability` : The probability of precipitation, expressed as
    a number between 0 ≤ precipitationProbability ≤ 1.

    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Optional

-   `windDirection` : Wind direction forecasted

    -   See [WeatherObserved.windDirection](../WeatherObserved/README.md)
        for description and units.
    -   Optional

-   `windSpeed` : Wind speed forecasted.

    -   See [WeatherObserved.windSpeed](../WeatherObserved/README.md) for
        description and units.
    -   Optional

-   `dayMinimum` : Minimum values forecasted for the reported period.

    -   Attribute type: Property. [StructuredValue](https://schema.org/StructuredValue)
    -   Subattributes:
        -   `temperature` : Minimum temperature. Same semantics and units as
            `WeatherForecast.temperature`.
        -   `feelLikesTemperature`. Minimum feels like temperature. Same
            semantics and units as `WeatherForecast.feelsLikeTemperature`.
        -   `relativeHumidity`. Minimum relative humidity. Same semantics and
            units as `WeatherForecast.relativeHumidity`.
    -   Optional

-   `dayMaximum` : Maximum values for the reported period.

    -   Attribute type: Property. [StructuredValue](https://schema.org/StructuredValue)
    -   Subattributes:
        -   `temperature` : Maximum temperature. See
            `WeatherForecast.temperature` for description and units.
        -   `feelLikesTemperature`. Maximum feels like temperature. Same
            semantics and units as `WeatherForecast.feelsLikeTemperature`.
        -   `relativeHumidity`. Maximum relative humidity. Same semantics and
            units as `WeatherForecast.relativeHumidity`.

-   `uVIndexMax` : The maximum UV index for the period, based on the World
    Health Organization's UV Index measure.
    -   Normative references:
        [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)
    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Optional
    -   Minimum 0

