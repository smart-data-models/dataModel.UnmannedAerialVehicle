<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: UnmannedAerialVehicleModel    
===================================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleModel/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Modells eines unbemannten Luftfahrzeugs (UAV) und ist anwendbar auf UAV-Befehls- und Kontrollanwendungen und damit verbundene UAV-Transportanwendungen**.    
Version: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Eine Beschreibung des Markennamens dieses unbemannten Luftfahrzeugmodells  - `categoryUAV[string]`: Die Arbeitskategorie des UAVModells. Eine Auswahl aus der folgenden Liste:'aerialPhotography, plantProtection, industry, routingInspection, mailing, transportation'.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `documentation[string]`: URI-Verweis (URL/URN) auf das Produktdatenblatt oder andere Herstellerunterlagen zu diesem unbemannten Luftfahrzeugmodell  - `fuelType[string]`: Die Treibstoffart, die das UAVModel antreibt. Eine Auswahl aus einer Aufzählungsliste, die die Energiequelle beschreibt. Enum:'gasoline, petrol(unleaded), petrol(leaded), petrol, diesel, electric, hydrogen, lpg autogas, cng, biodiesel, ethanol, hybrid electric/petrol, hybrid electric/diesel, other'  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manufacturerName[string]`: Der Name des Herstellers dieses unbemannten Luftfahrzeugmodells  - `maxFlightAltitude[number]`: Die maximale Flughöhe des unbemannten Luftfahrzeugmodells über dem Boden. Geben Sie Wert und Maßeinheiten an  - `maxFlightTime[number]`: Die maximale Flugdauer des unbemannten Luftfahrzeugmodells mit vollem Kraftstoff und ohne Last. Geben Sie Wert und Maßeinheiten an  - `maxGroundVelocity[number]`: Die maximale Bodengeschwindigkeit des unbemannten Luftfahrzeugmodells (bei Windstille). Geben Sie Wert und Maßeinheiten an  - `maxLoad[number]`: Die maximale Last, die das unbemannte Luftfahrzeug transportieren darf. Geben Sie Wert und Maßeinheiten an  - `minUnladenWeight[number]`: Das Gewicht des unbemannten Luftfahrzeugs mit vollem Kraftstoff, aber ohne Last. Geben Sie Wert und Maßeinheiten an  - `minWeight[number]`: Das Gewicht des unbemannten Luftfahrzeugs ohne Treibstoff oder Ladung. Geben Sie Wert und Maßeinheiten an  - `model[string]`: Die Kennung des UAV-Modells, die ein unbemanntes Luftfahrzeugmodell sein kann  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `rotors[number]`: Die Anzahl der Rotoren des unbemannten Luftfahrzeugs Modell  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI Entity-Kennung. Er muss UnmannedAerialVehicle lauten.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Dieses Datenmodell stammt aus dem ursprünglichen GSMA IoT-Projekt, https://www.gsma.com/iot/iot-big-data/. Es wurden einige kleinere Anpassungen vorgenommen, um den Anforderungen intelligenter Datenmodelle zu entsprechen.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
UnmannedAerialVehicleModel:      
  description: This entity contains a harmonised description of a generic Unmanned Ariel Vehicle (UAV) model and is applicable to UAV command and control and related UAV transport applications.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    brandName:      
      description: A description of the brand name of this Unmanned Aerial Vehicle Model      
      type: string      
      x-ngsi:      
        type: Property      
    categoryUAV:      
      description: 'The work category of the UAVModel. A choice from the following listnum:''aerialPhotography, plantProtection, industry, routingInspection, mailing, transportation'''      
      enum:      
        - aerialPhotography      
        - industry      
        - mailing      
        - plantProtection      
        - routingInspection      
        - transportation      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    documentation:      
      description: URI reference (URL/URN) to Product Data Sheet or other manufacturers documentation about this Unmanned Aerial Vehicle Model      
      type: string      
      x-ngsi:      
        type: Property      
    fuelType:      
      description: 'The fuel type powering the UAVModel. A choice from an enumerated list describing the power source. Enum:''gasoline, petrol(unleaded), petrol(leaded), petrol, diesel, electric, hydrogen, lpg autogas, cng, biodiesel, ethanol, hybrid electric/petrol, hybrid electric/diesel, other'''      
      enum:      
        - biodiesel      
        - cng      
        - diesel      
        - electric      
        - ethanol      
        - gasoline      
        - hybrid electric/petrol      
        - hybrid electric/diesel      
        - hydrogen      
        - lpgAutogas      
        - other      
        - petrol      
        - petrol(unleaded)      
        - petrol(leaded)      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    manufacturerName:      
      description: The name of the manufacturer of this Unmanned Aerial Vehicle Model      
      type: string      
      x-ngsi:      
        type: Property      
    maxFlightAltitude:      
      description: The maximum flight altitude of the Unmanned Aerial Vehicle Model above ground. Specify value and units of measure      
      type: number      
      x-ngsi:      
        type: Property      
    maxFlightTime:      
      description: The maximum duration of flight of the Unmanned Aerial Vehicle Model with full fuel and no load. Specify value and units of measure      
      type: number      
      x-ngsi:      
        type: Property      
    maxGroundVelocity:      
      description: The maximum ground velocity of the Unmanned Aerial Vehicle Model (under still wind conditions). Specify value and units of measure      
      type: number      
      x-ngsi:      
        type: Property      
    maxLoad:      
      description: The maximum load that the Unmanned Aerial Vehicle is permitted to transport. Specify value and units of measure      
      type: number      
      x-ngsi:      
        type: Property      
    minUnladenWeight:      
      description: The weight of the Unmanned Aerial Vehicle with full fuel but no load. Specify value and units of measure      
      type: number      
      x-ngsi:      
        type: Property      
    minWeight:      
      description: The weight of the Unmanned Aerial Vehicle without fuel or load. Specify value and units of measure      
      type: number      
      x-ngsi:      
        type: Property      
    model:      
      description: 'The UAV models identifier, which may be a Unmanned Aerial Vehicle Model'      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    rotors:      
      description: The number of the rotors of the Unmanned Aerial Vehicle Model      
      type: number      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity identifier. It has to be UnmannedAerialVehicle      
      enum:      
        - UnmannedAerialVehicleModel      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleModel/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicleModel/UnmannedAerialVehicleModel/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### UnmannedAerialVehicleModel NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleModel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVModel:6f4439d2-5925-11e8-a0ef-53719253dbbd",  
  "type": "UnmannedAerialVehicleModel",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "model": "ACME Recon",  
  "documentation": "http://example.com/products-services/aircraft/the-recon.html",  
  "description": "The Recon was constructed and designed to offer a clear payload view, with the motor and propeller system aft of the payload. It is smaller and more versatile than many drones, yet robust enough for harsh environment operations. The wingspan is 2.3 meters. An affordable, versatile, and flexible drone for a multitude of uses.",  
  "manufacturerName": "ACME UAVs",  
  "brandName": "Airv",  
  "categoryUAV": "aerialPhotography",  
  "rotors": 4,  
  "fuelType": "gasoline",  
  "maxFlightTime": 100,  
  "maxFlightAltitude": 1000,  
  "maxGroundVelocity": 100,  
  "minWeight": 1,  
  "minUnladenWeight": 1.5,  
  "maxLoad": 0.8  
}  
```  
</details>    
#### UnmannedAerialVehicleModel NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVModel:6f4439d2-5925-11e8-a0ef-53719253dbbd",  
  "type": "UnmannedAerialVehicleModel",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "model": {  
    "type": "Text",  
    "value": "ACME Recon"  
  },  
  "documentation": {  
    "type": "Text",  
    "value": "http://example.com/products-services/aircraft/the-recon.html"  
  },  
  "description": {  
    "type": "Text",  
    "value": "The Recon was constructed and designed to offer a clear payload view, with the motor and propeller system aft of the payload. It is smaller and more versatile than many drones, yet robust enough for harsh environment operations. The wingspan is 2.3 meters. An affordable, versatile, and flexible drone for a multitude of uses."  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "ACME UAVs"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Airv"  
  },  
  "categoryUAV": {  
    "type": "Text",  
    "value": "aerialPhotography"  
  },  
  "rotors": {  
    "type": "Number",  
    "value": 4  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "gasoline"  
  },  
  "maxFlightTime": {  
    "type": "Number",  
    "value": 100  
  },  
  "maxFlightAltitude": {  
    "type": "Number",  
    "value": 1000  
  },  
  "maxGroundVelocity": {  
    "type": "Number",  
    "value": 100  
  },  
  "minWeight": {  
    "type": "Boolean",  
    "value": true  
  },  
  "minUnladenWeight": {  
    "type": "Number",  
    "value": 1.5  
  },  
  "maxLoad": {  
    "type": "Number",  
    "value": 0.8  
  }  
}  
```  
</details>    
#### UnmannedAerialVehicleModel NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleModel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicleModel/UnmannedAerialVehicleModel/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:UAVModel:6f4439d2-5925-11e8-a0ef-53719253dbbd",  
  "type": "UnmannedAerialVehicleModel",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "model": "ACME Recon",  
  "documentation": "http://example.com/products-services/aircraft/the-recon.html",  
  "description": "The Recon was constructed and designed to offer a clear payload view, with the motor and propeller system aft of the payload. It is smaller and more versatile than many drones, yet robust enough for harsh environment operations. The wingspan is 2.3 meters. An affordable, versatile, and flexible drone for a multitude of uses.",  
  "manufacturerName": "ACME UAVs",  
  "brandName": "Airv",  
  "categoryUAV": "aerialPhotography",  
  "rotors": 4,  
  "fuelType": "gasoline",  
  "maxFlightTime": 100,  
  "maxFlightAltitude": 1000,  
  "maxGroundVelocity": 100,  
  "minWeight": 1,  
  "minUnladenWeight": 1.5,  
  "maxLoad": 0.8  
}  
```  
</details>    
#### UnmannedAerialVehicleModel NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleModel im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicleModel/UnmannedAerialVehicleModel/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:UAVModel:6f4439d2-5925-11e8-a0ef-53719253dbbd",  
    "type": "UnmannedAerialVehicleModel",  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "model": {  
        "type": "Property",  
        "value": "ACME Recon"  
    },  
    "documentation": {  
        "type": "Property",  
        "value": {  
            "@value": "http://example.com/products-services/aircraft/the-recon.html",  
            "@type": "https://schema.org/url"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "The Recon was constructed and designed to offer a clear payload view, with the motor and propeller system aft of the payload. It is smaller and more versatile than many drones, yet robust enough for harsh environment operations. The wingspan is 2.3 meters. An affordable, versatile, and flexible drone for a multitude of uses."  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "ACME UAVs"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Airv"  
    },  
    "categoryUAV": {  
        "type": "Property",  
        "value": "aerialPhotography"  
    },  
    "rotors": {  
        "type": "Property",  
        "value": 4  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "gasoline"  
    },  
    "maxFlightTime": {  
        "type": "Property",  
        "value": 100,  
        "unitCode": "HUR"  
    },  
    "maxFlightAltitude": {  
        "type": "Property",  
        "value": 1000,  
        "unitCode": "MTR"  
    },  
    "maxGroundVelocity": {  
        "type": "Property",  
        "value": 100,  
        "unitCode": "MTS"  
    },  
    "minWeight": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "KGM"  
    },  
    "minUnladenWeight": {  
        "type": "Property",  
        "value": 1.5,  
        "unitCode": "KGM"  
    },  
    "maxLoad": {  
        "type": "Property",  
        "value": 0.8,  
        "unitCode": "KGM"  
    }  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
