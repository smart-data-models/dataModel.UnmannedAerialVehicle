<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=============================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  
	- `operatingSystem`:     
	- `softwareVersion`:     
- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
