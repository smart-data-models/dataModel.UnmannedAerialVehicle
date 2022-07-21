[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: UnmannedAerialVehicle  
==============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines bestimmten unbemannten Luftfahrzeugs (UAV). Diese Entität ist in erster Linie mit UAV-Kommando und -Kontrolle und damit verbundenen UAV-Transportanwendungen verbunden.**  
Version: 0.0.1  

## Liste der Eigenschaften  

- `UnmannedAerialVehicleModel`: Verweis auf die UAV-Modelldefinition, die das UAV näher beschreibt.  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `elevation`: Die Höhe des UAV (relativ zum Boden am angegebenen Standort). Geben Sie den Wert und die Maßeinheiten an.  - `flightStatus`: Der Flugstatus der UAV, einschließlich der folgenden. Enum:'stop, takeoff, flight, hover, land'  - `fuel`: Aktuelle Treibstoffmenge der UAV. Wert und Maßeinheiten angeben  - `groundSpeed`: Die zuletzt gemeldete Bodengeschwindigkeit des UAV. Geben Sie Wert und Maßeinheiten an  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `observedAt`: Gibt das Datum/die Uhrzeit des letzten Überwachungsberichts oder der letzten Aktualisierung an.  - `operationMode`: Text zur Beschreibung der Auswahl aus diesen Werten. Enum:'vlos, evlos, bvlos, automated'. Hinweis: Die Beschreibungen stimmen mit der UTM-Flugmeldung überein.  - `operator`: Eine Liste mit Angaben zu dem oder den Betreibern der Drohne. Verweist auf eine oder mehrere Schema.org Personen oder Organisationen.https://schema.org/Personhttps://schema.org/Organization  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type`: NGSI Entity-Kennung. Er muss UnmannedAerialVehicle lauten.  - `workStatus`: Der Arbeitsstatus der UAV, einschließlich dieser. Enum:'stop, prepare, work, finish'    
Erforderliche Eigenschaften  
- `id`  - `type`    
Dieses Datenmodell stammt aus dem ursprünglichen GSMA IoT-Projekt, https://www.gsma.com/iot/iot-big-data/. Es wurden einige kleinere Anpassungen vorgenommen, um den Anforderungen intelligenter Datenmodelle zu entsprechen.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicle:    
  description: 'This entity contains a harmonised description of a specific Unmanned Aerial Vehicle (UAV). This entity is primarily associated with UAV command and control and related UAV transport applications.'    
  properties:    
    UnmannedAerialVehicleModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the UAV Model definition which describes the UAV in more detail.'    
      x-ngsi:    
        type: Relationship    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    elevation:    
      description: 'The elevation of the UAV (relative to ground level at the specified location). Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    flightStatus:    
      description: 'The flight status of the UAV, including these. Enum:''stop, takeoff, flight, hover, land'''    
      enum:    
        - flight    
        - hover    
        - land    
        - stop    
        - takeoff    
      type: string    
      x-ngsi:    
        type: Property    
    fuel:    
      description: 'Current fuel load of the UAV. Specify value and units of measure'    
      type: number    
      x-ngsi:    
        type: Property    
    groundSpeed:    
      description: 'The latest reported ground speed of the UAV. Specify value and units of measure'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &unmannedaerialvehicle_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observedAt:    
      description: 'Indicates the date/time of the latest monitoring report or update.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: 'Text describing the choice from these values. Enum:''vlos, evlos, bvlos, automated''. Note: descriptions align with UTM Flight message.'    
      enum:    
        - vlos    
        - evlos    
        - bvlos    
        - automated    
      type: string    
      x-ngsi:    
        type: Property    
    operator:    
      description: 'A list detailing the operator or operators of the UAV. Refers to one or more Schema.org person or organization.https://schema.org/Personhttps://schema.org/Organization'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *unmannedaerialvehicle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be UnmannedAerialVehicle'    
      enum:    
        - UnmannedAerialVehicle    
      type: string    
      x-ngsi:    
        type: Property    
    workStatus:    
      description: 'The work status of the UAV, including these. Enum:''stop, prepare, work, finish'''    
      enum:    
        - finish    
        - prepare    
        - stop    
        - work    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicle/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Beispiel-Nutzlasten  
#### UnmannedAerialVehicle NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein UnmannedAerialVehicle im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:UAV:1fa179a6-b507-4857-ad72-eb5513ef05c6",  
  "type": "UnmannedAerialVehicle",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "uavModel": "urn:ngsi-ld:UAVModel:23821045-33d4-46ec-b777-98f461bf4856",  
  "name": "Yellow1",  
  "owner": [  
    "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld:Organization:1be9cd61-ef59-421f-a326-4b6c84411ad4"  
  ],  
  "operator": [  
    "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld:Person:3d5f533e-5920-11e8-871b-534f1ae5f35d"  
  ],  
  "operationMode": "vlos",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "elevation": 1000,  
  "observedAt": "2016-08-23T10:18:16Z",  
  "flightStatus": "takeoff",  
  "workStatus": "finish",  
  "groundSpeed": 50,  
  "fuel": 50  
}  
```  
#### UnmannedAerialVehicle NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein UnmannedAerialVehicle im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:UAV:1fa179a6-b507-4857-ad72-eb5513ef05c6",  
  "type": "UnmannedAerialVehicle",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "uavModel": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:UAVModel:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Yellow1"  
  },  
  "owner": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:Organization:1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "operator": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:Person:3d5f533e-5920-11e8-871b-534f1ae5f35d"  
    ]  
  },  
  "operationMode": {  
    "type": "Text",  
    "value": "vlos"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "elevation": {  
    "type": "Number",  
    "value": 1000  
  },  
  "observedAt": {  
    "type": "DateTime",  
    "value": "2016-08-23T10:18:16Z"  
  },  
  "flightStatus": {  
    "type": "Text",  
    "value": "takeoff"  
  },  
  "workStatus": {  
    "type": "Text",  
    "value": "finish"  
  },  
  "groundSpeed": {  
    "type": "Number",  
    "value": 50  
  },  
  "fuel": {  
    "type": "Number",  
    "value": 50  
  }  
}  
```  
#### UnmannedAerialVehicle NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein UnmannedAerialVehicle im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.json"  
  ],  
  "id": "urn:ngsi-ld:UAV:1fa179a6-b507-4857-ad72-eb5513ef05c6",  
  "type": "UnmannedAerialVehicle",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "uavModel": "urn:ngsi-ld:UAVModel:23821045-33d4-46ec-b777-98f461bf4856",  
  "name": "Yellow1",  
  "owner": [  
    "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld:Organization:1be9cd61-ef59-421f-a326-4b6c84411ad4"  
  ],  
  "operator": [  
    "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
    "urn:ngsi-ld:Person:3d5f533e-5920-11e8-871b-534f1ae5f35d"  
  ],  
  "operationMode": "vlos",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "elevation": 1000,  
  "observedAt": "2016-08-23T10:18:16Z",  
  "flightStatus": "takeoff",  
  "workStatus": "finish",  
  "groundSpeed": 50,  
  "fuel": 50  
}  
```  
#### UnmannedAerialVehicle NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein UnmannedAerialVehicle im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.json"  
  ],  
  "id": "urn:ngsi-ld:UAV:1fa179a6-b507-4857-ad72-eb5513ef05c6",  
  "type": "UnmannedAerialVehicle",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "uavModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:UAVModel:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Yellow1"  
  },  
  "owner": {  
    "type": "Property",  
    "object": [  
      "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:Organization:1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "operator": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:Person:3d5f533e-5920-11e8-871b-534f1ae5f35d"  
    ]  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "vlos"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "elevation": {  
    "type": "Property",  
    "value": 1000,  
    "unitCode": "MTR"  
  },  
  "observedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-23T10:18:16Z"  
    }  
  },  
  "flightStatus": {  
    "type": "Property",  
    "value": "takeoff"  
  },  
  "workStatus": {  
    "type": "Property",  
    "value": "finish"  
  },  
  "groundSpeed": {  
    "type": "Property",  
    "value": 50,  
    "unitText": "MTS"  
  },  
  "fuel": {  
    "type": "Property",  
    "value": 50,  
    "unitCode": "GLI"  
  }  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
