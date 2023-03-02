/* (Beta) Export of data model WeatherObserved of the subject dataModel.Weather for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WeatherObserved_type AS ENUM ('WeatherObserved');
CREATE TABLE WeatherObserved (address json, airQualityIndex text, airQualityIndexForecast text, airTemperatureForecast text, airTemperatureTSA json, alternateName text, aqiMajorPollutant text, aqiMajorPollutantForecast text, areaServed text, atmosphericPressure text, dataProvider text, dateCreated timestamp, dateModified timestamp, dateObserved timestamp, description text, dewPoint text, feelLikesTemperature text, gustSpeed text, id text, illuminance text, location json, name text, owner json, precipitation text, precipitationForecast text, pressureTendency json, refDevice text, refPointOfInterest text, relativeHumidity text, relativeHumidityForecast text, seeAlso json, snowHeight text, solarRadiation text, source text, streamGauge text, temperature text, type WeatherObserved_type, uVIndexMax text, visibility json, weatherType text, windDirection text, windSpeed text);