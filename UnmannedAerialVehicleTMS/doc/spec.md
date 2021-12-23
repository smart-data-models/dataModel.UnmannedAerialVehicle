Entity: UnmannedAerialVehicleTMS  
================================  
[Open License](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMS/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonized description of a specific Unmanned Aerial Vehicle (UAV) Traffic Management Software Application that is designed to listen to and monitor the information transmitted by UAV’s, typically this software application would be operated at a ground station. This entity is primarily associated with UAV command and control applications.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `operationalInstance`: URL linking to an operational instance (assumed to be web based) for the UAV Traffic Management Software.  - `operator`: A list detailing the operator or operators of the UAV. Refers to one or more Schema.org person or organization.https://schema.org/Person or https://schema.org/Organization  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `softwareApplication`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity identifier. It has to be UnmannedAerialVehicleTMS    
Required properties  
- `id`  - `required`    
This data model comes from the original project GSMA IoT project, https://www.gsma.com/iot/iot-big-data/. There are some minor adaptations to meet requirements of smart data models.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### UnmannedAerialVehicleTMS NGSI-v2 key-values Example    
Here is an example of a UnmannedAerialVehicleTMS in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### UnmannedAerialVehicleTMS NGSI-v2 normalized Example    
Here is an example of a UnmannedAerialVehicleTMS in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### UnmannedAerialVehicleTMS NGSI-LD key-values Example    
Here is an example of a UnmannedAerialVehicleTMS in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.jsonld"  
  ]  
}  
```  
#### UnmannedAerialVehicleTMS NGSI-LD normalized Example    
Here is an example of a UnmannedAerialVehicleTMS in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/context.jsonld"  
  ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
