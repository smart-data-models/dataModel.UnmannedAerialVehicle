<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: UnmannedAerialVehicle  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esta entidad contiene una descripción armonizada de un vehículo aéreo no tripulado (UAV) específico. Esta entidad se asocia principalmente a las aplicaciones de mando y control de UAV y de transporte de UAV relacionados.**.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `UnmannedAerialVehicleModel[*]`: Referencia a la definición del modelo de UAV que describe el UAV con más detalle  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `elevation[number]`: La elevación del UAV (relativa al nivel del suelo en la ubicación especificada). Especifique el valor y las unidades de medida  - `flightStatus[string]`: El estado de vuelo del UAV, incluyendo estos. Enum:'parada, despegue, vuelo, planeo, aterrizaje'.  - `fuel[number]`: Carga actual de combustible del UAV. Especificar valor y unidades de medida  - `groundSpeed[number]`: La última velocidad en tierra del UAV. Especifique el valor y las unidades de medida  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `observedAt[date-time]`: Indica la fecha/hora del último informe de seguimiento o actualización  - `operationMode[string]`: Texto que describe la elección entre estos valores. Enum:'vlos, evlos, bvlos, automated'. Nota: las descripciones coinciden con el mensaje UTM Flight.  - `operator[array]`: Lista que detalla el operador u operadores del UAV. Hace referencia a una o varias personas u organizaciones de Schema.org.https://schema.org/Personhttps://schema.org/Organization  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Identificador de entidad NGSI. Tiene que ser UnmannedAerialVehicle  - `workStatus[string]`: El estado de trabajo del UAV, incluyendo estos. Enum:'parar, preparar, trabajar, terminar'.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Este modelo de datos procede del proyecto IoT original de la GSMA, https://www.gsma.com/iot/iot-big-data/. Hay algunas adaptaciones menores para cumplir los requisitos de los modelos de datos inteligentes.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicle:    
  description: This entity contains a harmonised description of a specific Unmanned Aerial Vehicle (UAV). This entity is primarily associated with UAV command and control and related UAV transport applications.    
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
    elevation:    
      description: The elevation of the UAV (relative to ground level at the specified location). Specify value and units of measure    
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
      description: Current fuel load of the UAV. Specify value and units of measure    
      type: number    
      x-ngsi:    
        type: Property    
    groundSpeed:    
      description: The latest reported ground speed of the UAV. Specify value and units of measure    
      type: number    
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
    observedAt:    
      description: Indicates the date/time of the latest monitoring report or update    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: 'Text describing the choice from these values. Enum:''vlos, evlos, bvlos, automated''. Note: descriptions align with UTM Flight message'    
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
      type: array    
      x-ngsi:    
        type: Relationship    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity identifier. It has to be UnmannedAerialVehicle    
      enum:    
        - UnmannedAerialVehicle    
      type: string    
      x-ngsi:    
        type: Property    
    uavModel:    
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
      description: Reference to the Unmanned Aerial Vehicle (UAV) Model definition which describes the UAV in more detail    
      x-ngsi:    
        type: Relationship    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicle/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### UnmannedAerialVehicle NGSI-v2 key-values Ejemplo  
A continuación se muestra un ejemplo de UnmannedAerialVehicle en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### UnmannedAerialVehicle NGSI-v2 normalizado Ejemplo  
A continuación se muestra un ejemplo de UnmannedAerialVehicle en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:UAV:1fa179a6-b507-4857-ad72-eb5513ef05c6",  
  "type": "UnmannedAerialVehicle",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "uavModel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:UAVModel:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Yellow1"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:Organization:1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "operator": {  
    "type": "StructuredValue",  
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
</details>  
#### UnmannedAerialVehicle NGSI-LD key-values Ejemplo  
A continuación se muestra un ejemplo de UnmannedAerialVehicle en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.json",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
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
</details>  
#### UnmannedAerialVehicle NGSI-LD normalizado Ejemplo  
A continuación se muestra un ejemplo de UnmannedAerialVehicle en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.json",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
