/* (Beta) Export of data model UnmannedAerialVehicle of the subject dataModel.UnmannedAerialVehicle for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE UnmannedAerialVehicle_flightStatus_type AS ENUM ('flight', 'hover', 'land', 'stop', 'takeoff');
CREATE TYPE UnmannedAerialVehicle_operationMode_type AS ENUM ('vlos', 'evlos', 'bvlos', 'automated');
CREATE TYPE UnmannedAerialVehicle_type AS ENUM ('UnmannedAerialVehicle');
CREATE TYPE UnmannedAerialVehicle_workStatus_type AS ENUM ('finish', 'prepare', 'stop', 'work');
CREATE TABLE UnmannedAerialVehicle (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "elevation" NUMERIC,
  "flightStatus" UnmannedAerialVehicle_flightStatus_type,
  "fuel" NUMERIC,
  "groundSpeed" NUMERIC,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "name" TEXT,
  "observedAt" TIMESTAMP,
  "operationMode" UnmannedAerialVehicle_operationMode_type,
  "operator" JSON,
  "owner" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "type" UnmannedAerialVehicle_type,
  "uavModel" JSON,
  "workStatus" UnmannedAerialVehicle_workStatus_type
);