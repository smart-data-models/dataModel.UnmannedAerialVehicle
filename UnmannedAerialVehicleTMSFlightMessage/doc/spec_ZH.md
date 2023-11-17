<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：无人驾驶飞行器 TMSFlightMessage    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMSFlightMessage/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**该实体包含通用无人机 UTM 飞行报文的统一描述，其中包含全球 UTM 关联协议报文。该实体主要与无人机的控制和管理有关。每个 UnmannedAerialVehicleTMSFlightMessage 实例都与特定的无人飞行器实例相关。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[date-time]`: 表示记录观察结果的日期/时间。请注意，该字段是为 NGSIv2 定义的，现已废弃。对于新实体和应用程序，请用 **observedAt** 代替。  - `description[string]`: 项目描述  - `flightMessage[object]`: 描述当前航班状态的航班信息，以全球UTM 信息的形式编码为一个 JSON 对象。 https://bitbucket.org/global_utm/flight-declaration-protocol  	- `flightDeclaration`:       
	- `flightId`:       
	- `sequenceNumber`:       
- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `observedAt[date-time]`: 表示 UAVFlightMessage 记录的日期/时间  - `originatedByUnmannedAutonomousVehicle[boolean]`: 信息来源的逻辑指标。真表示是无人机本身，假表示是另一个来源、监听站软件应用程序或不同的无人机  - `originator[*]`: 在信息并非由无人机直接发出的情况下，指报告信息的第三方无人机实例或其他实体（如监听站）。  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体标识符。必须是 UnmannedAerialVehicleTMSFlightMessage。  - `unmannedAerialVehicle[*]`: 与此 UAVFlightMessage 相关的 UAV 实体的引用  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该数据模型来自 GSMA 物联网项目的原始项目 https://www.gsma.com/iot/iot-big-data/。为满足智能数据模型的要求，本数据模型略有改动。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
UnmannedAerialVehicleTMSFlightMessage:      
  description: 'This entity contains a harmonised description of a generic UAV UTM Flight Message, which contains a Global UTM Association protocol message. This entity is primarily associated with the control and management of Unmanned Aerial Vehicles. Each UnmannedAerialVehicleTMSFlightMessage instance is related to a specific UAV instance.'      
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
    dateObserved:      
      description: Indicates the date/time the observation was recorded.Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **observedAt**      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    flightMessage:      
      description: 'A flight message describing the current flight status encoded as a Global UTM Message encoded as a JSON object. https://bitbucket.org/global_utm/flight-declaration-protocol'      
      properties:      
        flightDeclaration:      
          properties:      
            actualLandingTime:      
              format: date-time      
              type: string      
            actualTakeOffTime:      
              format: date-time      
              type: string      
            contactUrl:      
              format: uri      
              type: string      
            expectTelemetry:      
              type: boolean      
            idents:      
              items:      
                type: string      
              type: array      
            operationMode:      
              enum:      
                - vlos      
                - evlos      
                - bvlos      
                - automated      
              type: string      
            originatingParty:      
              type: string      
            parts:      
              items:      
                type: string      
              type: array      
            purpose:      
              type: string      
          type: object      
        flightId:      
          type: string      
        sequenceNumber:      
          type: number      
        version:      
          type: string      
      type: object      
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
      description: Indicates the date/time of the UAVFlightMessage record      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    originatedByUnmannedAutonomousVehicle:      
      description: 'A logical indicator of source of the message. True indicates it is the UAV itself, false indicates that it is a different source, a listening station software application or a different UAV'      
      type: boolean      
      x-ngsi:      
        type: Property      
    originator:      
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
      description: Refers to a third party UAV instance or other entity (e.g. listening station) that reported the information in the case the message was not directly originated by the UAV      
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
      description: NGSI Entity identifier. It has to be UnmannedAerialVehicleTMSFlightMessage      
      enum:      
        - UnmannedAerialVehicleTMSFlightMessage      
      type: string      
      x-ngsi:      
        type: Property      
    unmannedAerialVehicle:      
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
      description: Reference to the UAV entity to which this UAVFlightMessage relates      
      x-ngsi:      
        type: Relationship      
  required: []      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMSFlightMessage/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMSFlightMessage/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### UnmannedAerialVehicleTMSFlightMessage NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 UnmannedAerialVehicleTMSFlightMessage 示例。当使用 "options=keyValues "时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVUTMFlightMessage:4de63bda-592c-11e8-a603-234826e9b9fe",  
  "type": "UnmannedAerialVehicleTMSFlightMessage",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "unmannedAerialVehicle": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "observedAt": "2016-08-23T10:18:16Z",  
  "originatedByUnmannedAutonomousVehicle": false,  
  "originator": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec",  
  "flightMessage": {  
    "flightId": "3ce68ac8-5932-11e8-9a8d-ef74eb0fb0a2",  
    "sequenceNumber": 0,  
    "flightDeclaration": {},  
    "version": "1.0.0"  
  }  
}  
```  
</details>    
#### UnmannedAerialVehicleTMSFlightMessage NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 UnmannedAerialVehicleTMSFlightMessage 示例。在不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVUTMFlightMessage:4de63bda-592c-11e8-a603-234826e9b9fe",  
  "type": "UnmannedAerialVehicleTMSFlightMessage",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "unmannedAerialVehicle": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "observedAt": {  
    "type": "DateTime",  
    "value": "2016-08-23T10:18:16Z"  
  },  
  "originatedByUnmannedAutonomousVehicle": {  
    "type": "Boolean",  
    "value": false  
  },  
  "originator": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec"  
  },  
  "flightMessage": {  
    "type": "StructuredValue",  
    "value": {  
      "flightId": "3ce68ac8-5932-11e8-9a8d-ef74eb0fb0a2",  
      "sequenceNumber": 0,  
      "flightDeclaration": {},  
      "version": "1.0.0"  
    }  
  }  
}  
```  
</details>    
#### UnmannedAerialVehicleTMSFlightMessage NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 UnmannedAerialVehicleTMSFlightMessage 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVUTMFlightMessage:4de63bda-592c-11e8-a603-234826e9b9fe",  
  "type": "UnmannedAerialVehicleTMSFlightMessage",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "unmannedAerialVehicle": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "observedAt": "2016-08-23T10:18:16Z",  
  "originatedByUnmannedAutonomousVehicle": false,  
  "originator": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec",  
  "flightMessage": {  
    "flightId": "3ce68ac8-5932-11e8-9a8d-ef74eb0fb0a2",  
    "sequenceNumber": 0,  
    "flightDeclaration": {},  
    "version": "1.0.0"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMSFlightMessage/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### UnmannedAerialVehicleTMSFlightMessage NGSI-LD 归一化示例    
下面是一个以 JSON-LD 格式规范化的 UnmannedAerialVehicleTMSFlightMessage 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:UAVUTMFlightMessage:4de63bda-592c-11e8-a603-234826e9b9fe",  
    "type": "UnmannedAerialVehicleTMSFlightMessage",  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "unmannedAerialVehicle": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
    },  
    "observedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-23T10:18:16Z"  
        }  
    },  
    "originatedByUnmannedAutonomousVehicle": {  
        "type": "Property",  
        "value": false  
    },  
    "originator": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec"  
    },  
    "flightMessage": {  
        "type": "Property",  
        "value": {  
            "flightId": "3ce68ac8-5932-11e8-9a8d-ef74eb0fb0a2",  
            "sequenceNumber": 0,  
            "flightDeclaration": {},  
            "version": "1.0.0"  
        }  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMSFlightMessage/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
