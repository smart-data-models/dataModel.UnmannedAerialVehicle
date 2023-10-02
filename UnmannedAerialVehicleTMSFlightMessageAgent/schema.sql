/* (Beta) Export of data model UnmannedAerialVehicleTMSFlightMessageAgent of the subject dataModel.UnmannedAerialVehicle for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE UnmannedAerialVehicleTMSFlightMessageAgent_type AS ENUM ('UnmannedAerialVehicleTMSFlightMessageAgent');
CREATE TABLE UnmannedAerialVehicleTMSFlightMessageAgent (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, flightControlPolicy TEXT, flightMessage JSON, name TEXT, observedAt TIMESTAMP, originatedByUnmannedAerialVehicle BOOLEAN, owner JSON, source TEXT, type UnmannedAerialVehicleTMSFlightMessageAgent_type, validationResult BOOLEAN);