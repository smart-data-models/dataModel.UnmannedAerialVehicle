Entità: UnmannedAerialVehicleEvent  
==================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleEvent/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **L'evento UAVE registra l'incursione di uno specifico UAV in uno spazio aereo protetto o in prossimità di esso. Registra anche la misura di controllo adottata. Questa entità è principalmente associata al comando e controllo UAV e alle relative applicazioni di trasporto UAV.  

## Elenco delle proprietà  

- `UnmannedAerialVehicle`: Riferimento all'entità UnmannedAerialVehicle a cui si riferisce questo evento.  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `elevation`: L'elevazione dell'UAV (rispetto al livello del suolo nella posizione specificata). Specificare il valore e le unità di misura.  - `endAt`: Indica la data/ora di quando l'evento è finito (se è finito).  - `eventResult`: Il risultato della gestione dell'evento, una scelta da questa lista, Enum:'logged, notify, alarm, forceLand, forceBack, forceHover'  - `eventType`: Il tipo di evento UAV, una scelta dalla lista. Enum:'illegalFlight, closeToUnperpermittedAirspace, overSpeed, overHeight, illegalWork'  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `originator`: Si riferisce a un'istanza UAV terza o a un'altra entità (per esempio una stazione di ascolto) che ha riportato l'informazione nel caso in cui l'evento non sia stato originato direttamente dall'UAV.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `startAt`: Indica la data/ora di inizio dell'evento.  - `type`: Identificatore di entità NGSI. Deve essere UnmannedAerialVehicleEvent    
Proprietà richieste  
- `id`  - `type`    
Questo modello di dati proviene dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Ci sono alcuni adattamenti minori per soddisfare i requisiti dei modelli di dati intelligenti.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicleEvent:    
  description: 'The UAVEvent records the incursion of a specific UAV into or near protected airspace or locations. It also records the control measure taken. This entity is primarily associated with UAV command and control and related UAV transport applications.'    
  properties:    
    UnmannedAerialVehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the UnmannedAerialVehicle entity to which this event relates.'    
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
    endAt:    
      description: 'Indicates the date/time of when the event ended (if it has ended).'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    eventResult:    
      description: 'The handling result of the event, a choice from ths list, Enum:''logged, notify, alarm, forceLand, forceBack, forceHover'''    
      enum:    
        - alarm    
        - forceBack    
        - forceHover    
        - forceLand    
        - logged    
        - notify    
      type: string    
      x-ngsi:    
        type: Property    
    eventType:    
      description: 'The type of the UAV event, a choice from the list. Enum:''illegalFlight, closeToUnpermittedAirspace, overSpeed, overHeight, illegalWork'''    
      enum:    
        - illegalFlight    
        - closeToUnpermittedAirspace    
        - overSpeed    
        - overHeight    
        - illegalWork    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &unmannedaerialvehicleevent_-_properties_-_owner_-_items_-_anyof    
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
    originator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Refers to a third party UAV instance or other entity (e.g. listening station) that reported the information in the case the event was not directly originated by the UAV.'    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *unmannedaerialvehicleevent_-_properties_-_owner_-_items_-_anyof    
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
    startAt:    
      description: 'Indicates the date/time of when the event started.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be UnmannedAerialVehicleEvent'    
      enum:    
        - UnmannedAerialVehicleEvent    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleEvent/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleEvent/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### UnmannedAerialVehicleEvent NGSI-v2 valori chiave Esempio  
Ecco un esempio di un UnmannedAerialVehicleEvent in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:UAVEvent:85df05a8-5922-11e8-ad9c-d7fa968d409d",  
  "type": "UnmannedAerialVehicleEvent",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "UnmannedAerialVehicle": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "originator": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "elevation": 1000,  
  "startAt": "2016-08-23T10:18:16Z",  
  "endAt": "2016-08-23T10:19:16Z",  
  "eventType": "overHeight",  
  "description": "The UAV is flying over a mandatory height limit",  
  "eventResult": "forceBack"  
}  
```  
#### UnmannedAerialVehicleEvent NGSI-v2 normalizzato Esempio  
Ecco un esempio di un UnmannedAerialVehicleEvent in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:UAVEvent:85df05a8-5922-11e8-ad9c-d7fa968d409d",  
  "type": "UnmannedAerialVehicleEvent",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "UnmannedAerialVehicle": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "originator": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
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
    "type": "numer",  
    "value": 1000  
  },  
  "startAt": {  
    "type": "DateTime",  
    "value": "2016-08-23T10:18:16Z"  
  },  
  "endAt": {  
    "type": "DateTime",  
    "value": "2016-08-23T10:19:16Z"  
  },  
  "eventType": {  
    "type": "Text",  
    "value": "overHeight"  
  },  
  "description": {  
    "type": "Text",  
    "value": "The Unmanned Aerial Vehicle is flying over a mandatory height limit"  
  },  
  "eventResult": {  
    "type": "Text",  
    "value": "forceBack"  
  }  
}  
```  
#### UnmannedAerialVehicleEvent NGSI-LD valori chiave Esempio  
Ecco un esempio di un UnmannedAerialVehicleEvent in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleEvent/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:UAVEvent:85df05a8-5922-11e8-ad9c-d7fa968d409d",  
  "type": "UnmannedAerialVehicleEvent",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "UnmannedAerialVehicle": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "originator": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "elevation": 1000,  
  "startAt": "2016-08-23T10:18:16Z",  
  "endAt": "2016-08-23T10:19:16Z",  
  "eventType": "overHeight",  
  "description": "The UAV is flying over a mandatory height limit",  
  "eventResult": "forceBack"  
}  
```  
#### UnmannedAerialVehicleEvent NGSI-LD normalizzato Esempio  
Ecco un esempio di un UnmannedAerialVehicleEvent in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleEvent/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:UAVEvent:85df05a8-5922-11e8-ad9c-d7fa968d409d",  
  "type": "UnmannedAerialVehicleEvent",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "UnmannedAerialVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "originator": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
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
  "startAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-23T10:18:16Z"  
    }  
  },  
  "endAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-23T10:19:16Z"  
    }  
  },  
  "eventType": {  
    "type": "Property",  
    "value": "overHeight"  
  },  
  "description": {  
    "type": "Property",  
    "value": "The Unmanned Aerial Vehicle is flying over a mandatory height limit"  
  },  
  "eventResult": {  
    "type": "Property",  
    "value": "forceBack"  
  }  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza