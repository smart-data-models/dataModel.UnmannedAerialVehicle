<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: UnmannedAerialVehicleTMS  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMS/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una specifica applicazione software per la gestione del traffico dei veicoli aerei senza pilota (UAV), progettata per ascoltare e monitorare le informazioni trasmesse dagli UAV. Questa entità è principalmente associata alle applicazioni di comando e controllo degli UAV **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `operationalInstance[string]`: URL di collegamento a un'istanza operativa (si presume basata sul web) del software di gestione del traffico UAV.  - `operator[array]`: Un elenco che indica l'operatore o gli operatori dell'UAV. Si riferisce a una o più persone o organizzazioni di Schema.org.https://schema.org/Person o https://schema.org/Organization  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `softwareApplication[object]`:   . Model: [Details about the software application using the Schema.org definition https://schema.org/SoftwareApplication](Details about the software application using the Schema.org definition https://schema.org/SoftwareApplication)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Identificatore dell'entità NGSI. Deve essere UnmannedAerialVehicleTMS  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `required`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello di dati deriva dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Sono stati apportati alcuni piccoli adattamenti per soddisfare i requisiti dei modelli di dati intelligenti.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicleTMS:    
  description: 'This entity contains a harmonized description of a specific Unmanned Aerial Vehicle (UAV) Traffic Management Software Application that is designed to listen to and monitor the information transmitted by UAV’s, typically this software application would be operated at a ground station. This entity is primarily associated with UAV command and control applications.'    
  properties:    
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
    id:    
      anyOf: &unmannedaerialvehicletms_-_properties_-_operator_-_items_-_anyof    
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationalInstance:    
      description: 'URL linking to an operational instance (assumed to be web based) for the UAV Traffic Management Software.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    operator:    
      description: 'A list detailing the operator or operators of the UAV. Refers to one or more Schema.org person or organization.https://schema.org/Person or https://schema.org/Organization'    
      items:    
        anyOf: *unmannedaerialvehicletms_-_properties_-_operator_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *unmannedaerialvehicletms_-_properties_-_operator_-_items_-_anyof    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be UnmannedAerialVehicleTMS'    
      enum:    
        - UnmannedAerialVehicleTMS    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - required    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## Esempi di payload  
#### UnmannedAerialVehicleTMS Valori chiave NGSI-v2 Esempio  
Ecco un esempio di UnmannedAerialVehicleTMS in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
  "type": "UAVUnmannedAerialVehicleTMS",  
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
#### UnmannedAerialVehicleTMS NGSI-v2 normalizzato Esempio  
Ecco un esempio di UnmannedAerialVehicleTMS in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
  "type": "UAVUnmannedAerialVehicleTMS",  
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
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
      "urn:ngsi-ld:Organization:c5d75a1c-592b-11e8-8a09-3bd13644426b"  
    ]  
  },  
  "operator": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Person:bd710472-592b-11e8-852c-6fd149eae28a",  
      "urn:ngsi-ld:Person:cbec3f1c-592b-11e8-943c-57802974f852"  
    ]  
  }  
}  
```  
</details>  
#### UnmannedAerialVehicleTMS Valori chiave NGSI-LD Esempio  
Ecco un esempio di UnmannedAerialVehicleTMS in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
    "type": "UAVUnmannedAerialVehicleTMS",  
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
#### UnmannedAerialVehicleTMS NGSI-LD normalizzato Esempio  
Ecco un esempio di UnmannedAerialVehicleTMS in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UAVTMS:e0ad01b2-592a-11e8-bf93-cf2039a6c0cf",  
    "type": "UAVUnmannedAerialVehicleTMS",  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
