/* (Beta) Export of data model WeatherObserved of the subject dataModel.Weather for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WeatherObserved_type AS ENUM ('WeatherObserved');
CREATE TABLE WeatherObserved (address JSON, airQualityIndex NUMERIC, airQualityIndexForecast NUMERIC, airTemperatureForecast NUMERIC, airTemperatureTSA JSON, alternateName TEXT, aqiMajorPollutant TEXT, aqiMajorPollutantForecast TEXT, areaServed TEXT, atmosphericPressure NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, dateObserved TIMESTAMP, description TEXT, dewPoint NUMERIC, diffuseIrradiation NUMERIC, directIrradiation NUMERIC, feelsLikeTemperature NUMERIC, gustSpeed NUMERIC, id TEXT PRIMARY KEY, illuminance NUMERIC, location JSON, name TEXT, owner JSON, precipitation NUMERIC, precipitationForecast NUMERIC, pressureTendency JSON, refPointOfInterest TEXT, relativeHumidity NUMERIC, relativeHumidityForecast NUMERIC, seeAlso JSON, snowHeight NUMERIC, solarRadiation NUMERIC, source TEXT, streamGauge NUMERIC, temperature NUMERIC, type WeatherObserved_type, uVIndexMax NUMERIC, weatherType TEXT, windDirection NUMERIC, windSpeed NUMERIC);