<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: UnmannedAerialVehicleEvent  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleEvent/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El UAVEvent registra la incursión de un UAV específico en el espacio aéreo protegido o en sus proximidades. También registra la medida de control adoptada. Esta entidad se asocia principalmente a las aplicaciones de mando y control de los vehículos aéreos no tripulados y a las aplicaciones de transporte de los vehículos aéreos no tripulados relacionadas.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `UnmannedAerialVehicle[*]`: Referencia a la entidad UnmannedAerialVehicle a la que se refiere este evento.  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `elevation[number]`: La elevación del UAV (relativa al nivel del suelo en la ubicación especificada). Especifique el valor y las unidades de medida.  - `endAt[string]`: Indica la fecha/hora de finalización del evento (si ha terminado).  - `eventResult[string]`: El resultado del manejo del evento, una elección de esta lista, Enum:'logged, notify, alarm, forceLand, forceBack, forceHover'  - `eventType[string]`: El tipo de evento del UAV, una elección de la lista. Enum:'illegalFlight, closeToUnpermittedAirspace, overSpeed, overHeight, illegalWork'  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `originator[*]`: Se refiere a una instancia del UAV de un tercero u otra entidad (por ejemplo, una estación de escucha) que ha comunicado la información en el caso de que el evento no haya sido originado directamente por el UAV.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startAt[string]`: Indica la fecha/hora de inicio del evento.  - `type[string]`: Identificador de la entidad NGSI. Debe ser UnmannedAerialVehicleEvent  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Este modelo de datos procede del proyecto original de GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Hay algunas adaptaciones menores para cumplir los requisitos de los modelos de datos inteligentes.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### UnmannedAerialVehicleEvent NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un UnmannedAerialVehicleEvent en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### UnmannedAerialVehicleEvent NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un UnmannedAerialVehicleEvent en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### UnmannedAerialVehicleEvent NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un UnmannedAerialVehicleEvent en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleEvent/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
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
</details>  
#### UnmannedAerialVehicleEvent NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un UnmannedAerialVehicleEvent en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleEvent/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
