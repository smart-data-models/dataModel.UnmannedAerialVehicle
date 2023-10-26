<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: UnmannedAerialVehicleModel  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleModel/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 엔티티에는 일반 무인 항공기(UAV) 모델에 대한 조화로운 설명이 포함되어 있으며, 무인 항공기 지휘 및 제어 및 관련 무인 항공기 운송 애플리케이션에 적용할 수 있습니다.**  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 이 무인 항공기 모델의 브랜드 이름에 대한 설명입니다.  - `categoryUAV[string]`: UAVModel의 작업 카테고리입니다. 다음 목록에서 선택: '항공촬영, 식물보호, 산업, 경로점검, 우편물, 운송'  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `documentation[string]`: 이 무인 항공기 모델에 대한 제품 데이터 시트 또는 기타 제조업체 문서에 대한 URI 참조(URL/URN)  - `fuelType[string]`: UAV모델에 동력을 공급하는 연료 유형입니다. 동력원을 설명하는 열거형 목록에서 선택합니다. 열거형: '가솔린, 가솔린(무연), 가솔린(납), 가솔린, 디젤, 전기, 수소, LPG 오토가스, CNG, 바이오디젤, 에탄올, 하이브리드 전기/가솔린, 하이브리드 전기/디젤, 기타'  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `manufacturerName[string]`: 이 무인 항공기 모델의 제조업체 이름입니다.  - `maxFlightAltitude[number]`: 지상에서 무인 항공기 모델의 최대 비행 고도입니다. 값 및 측정 단위 지정  - `maxFlightTime[number]`: 연료를 가득 채우고 무부하 상태에서 무인 항공기 모델의 최대 비행 시간입니다. 값 및 측정 단위 지정  - `maxGroundVelocity[number]`: 무인 항공기 모델의 최대 지상 속도(정풍 조건에서)입니다. 값 및 측정 단위 지정  - `maxLoad[number]`: 무인 항공기가 운송할 수 있는 최대 적재량입니다. 값 및 측정 단위 지정  - `minUnladenWeight[number]`: 연료를 가득 채웠지만 하중이 없는 무인 항공기의 무게입니다. 값 및 측정 단위 지정  - `minWeight[number]`: 연료 또는 적재물을 제외한 무인 항공기의 무게입니다. 값 및 측정 단위 지정  - `model[string]`: 무인 항공기 모델 식별자(무인 항공기 모델일 수 있음)  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `rotors[number]`: 무인 항공기 모델의 로터 수입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 식별자. UnmannedAerialVehicle이어야 합니다.  <!-- /30-PropertiesList -->  
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
## 페이로드 예시  
#### UnmannedAerialVehicleModel NGSI-v2 키값 예시  
다음은 키-값으로 JSON-LD 형식의 UnmannedAerialVehicleModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### UnmannedAerialVehicleModel NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 UnmannedAerialVehicleModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:UAVModel:6f4439d2-5925-11e8-a0ef-53719253dbbd",  
  "type": "UnmannedAerialVehicleModel",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "model": {  
    "type": "Text",  
    "value": "ACME Recon"  
  },  
  "documentation": {  
    "type": "URL",  
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
    "type": "Number",  
    "value": 1  
  },  
  "minUnladenWeight": {  
    "type": "Number",  
    "value": 1.5  
  },  
  "maxLoad": {  
    "type": "Property",  
    "value": 0.8  
  }  
}  
```  
</details>  
#### UnmannedAerialVehicleModel NGSI-LD 키값 예시  
다음은 키값으로 JSON-LD 형식의 UnmannedAerialVehicleModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### UnmannedAerialVehicleModel NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 UnmannedAerialVehicleModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
