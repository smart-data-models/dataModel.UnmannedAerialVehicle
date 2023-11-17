<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: UnmannedAerialVehicle    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **이 엔티티에는 특정 무인 항공기(UAV)에 대한 조화로운 설명이 포함되어 있습니다. 이 엔티티는 주로 UAV 명령 및 제어 및 관련 UAV 운송 애플리케이션과 연관되어 있습니다.**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `UnmannedAerialVehicleModel[*]`: UAV를 더 자세히 설명하는 UAV 모델 정의 참조  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `elevation[number]`: UAV의 고도(지정된 위치의 지상 기준)입니다. 값 및 측정 단위 지정  - `flightStatus[string]`: 이를 포함한 UAV의 비행 상태입니다. Enum: '정지, 이륙, 비행, 호버링, 착륙'  - `fuel[number]`: 무인 항공기의 현재 연료 부하. 값 및 측정 단위 지정  - `groundSpeed[number]`: UAV의 최근 보고된 지상 속도입니다. 값 및 측정 단위 지정  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `observedAt[date-time]`: 최신 모니터링 보고서 또는 업데이트의 날짜/시간을 나타냅니다.  - `operationMode[string]`: 이러한 값 중에서 선택 사항을 설명하는 텍스트입니다. 열거형: 'vlos, evlos, bvlos, automated'. 참고: 설명은 UTM 항공편 메시지와 일치합니다.  - `operator[array]`: UAV의 운영자 또는 운영자를 자세히 설명하는 목록입니다. 하나 이상의 Schema.org 사용자 또는 조직을 참조합니다.https://schema.org/Personhttps://schema.org/Organization  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 식별자. UnmannedAerialVehicle이어야 합니다.  - `workStatus[string]`: 이를 포함한 UAV의 작업 상태입니다. Enum:'중지, 준비, 작업, 완료'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
이 데이터 모델은 원래 프로젝트인 GSMA IoT 프로젝트(https://www.gsma.com/iot/iot-big-data/)에서 가져온 것입니다. 스마트 데이터 모델의 요구 사항을 충족하기 위해 몇 가지 약간의 수정이 있었습니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
UnmannedAerialVehicle:      
  description: This entity contains a harmonised description of a specific Unmanned Aerial Vehicle (UAV). This entity is primarily associated with UAV command and control and related UAV transport applications.      
  properties:      
    UnmannedAerialVehicleModel:      
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
      description: Reference to the UAV Model definition which describes the UAV in more detail      
      x-ngsi:      
        type: Relationship      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicle/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### UnmannedAerialVehicle NGSI-v2 키값 예시    
다음은 키-값으로 JSON-LD 형식의 UnmannedAerialVehicle의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### UnmannedAerialVehicle NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 UnmannedAerialVehicle의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### UnmannedAerialVehicle NGSI-LD 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 UnmannedAerialVehicle의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### UnmannedAerialVehicle NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 UnmannedAerialVehicle의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
