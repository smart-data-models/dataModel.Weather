/* (Beta) Export of data model WeatherAlert of the subject dataModel.Weather for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE category_type AS ENUM ('traffic','naturalDisaster','weather','environment','health','security','agriculture');CREATE TYPE severity_type AS ENUM ('informational','low','medium','high','critical');CREATE TYPE subCategory_type AS ENUM ('avalanches','coastalEvent','coldWave','flood','fog','forestFire','heatWave','highTemperature','hurricane','ice','lowTemperature','rainfall','rain_flood','snow','snow_ice','thunderstorms','tornado','tropicalCyclone','tsunami','wind');CREATE TYPE WeatherAlert_type AS ENUM ('WeatherAlert');
CREATE TABLE WeatherAlert (address JSON, alternateName TEXT, areaServed TEXT, category category_type, data JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateIssued TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, severity severity_type, source TEXT, subCategory subCategory_type, type WeatherAlert_type, validFrom TIMESTAMP, validTo TIMESTAMP);