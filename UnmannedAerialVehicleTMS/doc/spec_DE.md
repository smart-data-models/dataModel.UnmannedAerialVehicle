<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: UnmannedAerialVehicleTMS    
=================================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMS/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung einer spezifischen Softwareanwendung für das Verkehrsmanagement von unbemannten Luftfahrzeugen (UAVs), die dazu dient, die von UAVs übermittelten Informationen abzuhören und zu überwachen. Diese Einheit wird in erster Linie mit UAV-Kommando und -Kontrollanwendungen in Verbindung gebracht.**    
Version: 0.0.1    
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
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße      
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `operationalInstance[uri]`: URL-Verknüpfung zu einer Betriebsinstanz (vermutlich webbasiert) für die UAV-Verkehrsmanagement-Software  - `operator[array]`: Eine Liste mit Angaben zu dem oder den Betreibern der Drohne. Verweist auf eine oder mehrere Schema.org Person oder Organisation.https://schema.org/Person oder https://schema.org/Organization  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `softwareApplication[object]`:   . Model: [Details about the software application using the Schema.org definition https://schema.org/SoftwareApplication](Details about the software application using the Schema.org definition https://schema.org/SoftwareApplication)	- `applicationCategory`:       
	- `operatingSystem`:       
	- `softwareVersion`:       
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Kennung der Entität. Er muss UnmannedAerialVehicleTMS lauten.  <!-- /30-PropertiesList -->    
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
UnmannedAerialVehicleTMS:      
  description: 'This entity contains a harmonized description of a specific Unmanned Aerial Vehicle (UAV) Traffic Management Software Application that is designed to listen to and monitor the information transmitted by UAV’s, typically this software application would be operated at a ground station. This entity is primarily associated with UAV command and control applications.'      
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
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationalInstance:      
      description: URL linking to an operational instance (assumed to be web based) for the UAV Traffic Management Software      
      format: uri      
      type: string      
      x-ngsi:      
        type: Property      
    operator:      
      description: 'A list detailing the operator or operators of the UAV. Refers to one or more Schema.org person or organization.https://schema.org/Person or https://schema.org/Organization'      
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
    softwareApplication:      
      description: ""      
      properties:      
        applicationCategory:      
          type: string      
        operatingSystem:      
          type: string      
        softwareVersion:      
          type: string      
      type: object      
      x-ngsi:      
        model: 'Details about the software application using the Schema.org definition https://schema.org/SoftwareApplication'      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity identifier. It has to be UnmannedAerialVehicleTMS      
      enum:      
        - UnmannedAerialVehicleTMS      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMS/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMS/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### UnmannedAerialVehicleTMS NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleTMS im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
  "type": "UnmannedAerialVehicleTMS",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "name": "PowerTMS",  
  "softwareApplication": {  
    "@type": "https://schema.org/SoftwareApplication",  
    "operatingSystem": "Linux",  
    "softwareVersion": "8.3",  
    "applicationCategory": "Guidance"  
  },  
  "operationalInstance": "http://example.com/uavtms",  
  "owner": [  
    "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
    "urn:ngsi-ld:Organization:c5d75a1c-592b-11e8-8a09-3bd13644426b"  
  ],  
  "operator": [  
    "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
    "urn:ngsi-ld:Person:cbec3f1c-592b-11e8-943c-57802974f852"  
  ]  
}  
```  
</details>    
#### UnmannedAerialVehicleTMS NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleTMS im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
  "type": "UnmannedAerialVehicleTMS",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "name": {  
    "type": "Text",  
    "value": "PowerTMS"  
  },  
  "softwareApplication": {  
    "type": "StructuredValue",  
    "value": {  
      "@type": "https://schema.org/SoftwareApplication",  
      "operatingSystem": "Linux",  
      "softwareVersion": "8.3",  
      "applicationCategory": "Guidance"  
    }  
  },  
  "operationalInstance": {  
    "type": "Text",  
    "value": "http://example.com/uavtms"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
      "urn:ngsi-ld:Organization:c5d75a1c-592b-11e8-8a09-3bd13644426b"  
    ]  
  },  
  "operator": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
      "urn:ngsi-ld:Person:cbec3f1c-592b-11e8-943c-57802974f852"  
    ]  
  }  
}  
```  
</details>    
#### UnmannedAerialVehicleTMS NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleTMS im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
  "type": "UnmannedAerialVehicleTMS",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "name": "PowerTMS",  
  "softwareApplication": {  
    "@type": "https://schema.org/SoftwareApplication",  
    "operatingSystem": "Linux",  
    "softwareVersion": "8.3",  
    "applicationCategory": "Guidance"  
  },  
  "operationalInstance": "http://example.com/uavtms",  
  "owner": [  
    "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
    "urn:ngsi-ld:Organization:c5d75a1c-592b-11e8-8a09-3bd13644426b"  
  ],  
  "operator": [  
    "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
    "urn:ngsi-ld:Person:cbec3f1c-592b-11e8-943c-57802974f852"  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### UnmannedAerialVehicleTMS NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein UnmannedAerialVehicleTMS im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
    "type": "UnmannedAerialVehicleTMS",  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "name": {  
        "type": "Property",  
        "value": "PowerTMS"  
    },  
    "softwareApplication": {  
        "type": "Property",  
        "value": {  
            "@type": "https://schema.org/SoftwareApplication",  
            "operatingSystem": "Linux",  
            "softwareVersion": "8.3",  
            "applicationCategory": "Guidance"  
        }  
    },  
    "operationalInstance": {  
        "type": "Property",  
        "value": "http://example.com/uavtms"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
            "urn:ngsi-ld:Organization:c5d75a1c-592b-11e8-8a09-3bd13644426b"  
        ]  
    },  
    "operator": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
            "urn:ngsi-ld:Person:cbec3f1c-592b-11e8-943c-57802974f852"  
        ]  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
    ]  
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
