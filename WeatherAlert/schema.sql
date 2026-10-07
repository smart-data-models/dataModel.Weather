/* (Beta) Export of data model WeatherAlert of the subject dataModel.Weather for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WeatherAlert_category_type AS ENUM ('agriculture', 'environment', 'health', 'naturalDisaster', 'security', 'traffic', 'weather');
CREATE TYPE WeatherAlert_severity_type AS ENUM ('informational', 'low', 'medium', 'high', 'critical');
CREATE TYPE WeatherAlert_subCategory_type AS ENUM ('avalanches', 'coastalEvent', 'coldWave', 'flood', 'fog', 'forestFire', 'heatWave', 'highTemperature', 'hurricane', 'ice', 'lowTemperature', 'rainfall', 'rain_flood', 'snow', 'snow_ice', 'thunderstorms', 'tornado', 'tropicalCyclone', 'tsunami', 'wind');
CREATE TYPE WeatherAlert_type AS ENUM ('WeatherAlert');
CREATE TABLE WeatherAlert (
  "address" JSON,
  "alertSource" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "category" WeatherAlert_category_type,
  "data" JSON,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateIssued" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "name" TEXT,
  "owner" JSON,
  "seeAlso" JSON,
  "severity" WeatherAlert_severity_type,
  "source" TEXT,
  "subCategory" WeatherAlert_subCategory_type,
  "type" WeatherAlert_type,
  "validFrom" TIMESTAMP,
  "validTo" TIMESTAMP
);