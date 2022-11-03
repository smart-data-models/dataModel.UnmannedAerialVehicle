<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。无人驾驶飞机模型（UnmannedAerialVehicleModel  
======================================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleModel/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该实体包含一个通用的无人飞行器（UAV）模型的统一描述，适用于无人飞行器的指挥和控制以及相关的无人飞行器运输应用。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 该无人驾驶航空器模型的品牌名称描述。  - `categoryUAV[string]`: UAVModel的工作类别。从以下列表中选择："空中摄影，植物保护，工业，路线检查，邮寄，运输  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `documentation[string]`: URI参考（URL/URN）到产品数据表或其他制造商关于此无人驾驶航空器模型的文件。  - `fuelType[string]`: 为UAVModel提供动力的燃料类型。从描述动力源的枚举列表中选择。Enum:'汽油，汽油（无铅），汽油（含铅），汽油，柴油，电动，氢气，液化石油气，CNG，生物柴油，乙醇，混合电动/汽油，混合电动/柴油，其他'  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `manufacturerName[string]`: 该无人驾驶航空器模型的制造商名称。  - `maxFlightAltitude[number]`: 无人驾驶飞行器模型离地面的最大飞行高度。指定数值和计量单位。  - `maxFlightTime[number]`: 无人驾驶飞行器模型在满油和无负载情况下的最大飞行时间。指定数值和计量单位。  - `maxGroundVelocity[number]`: 无人驾驶飞行器模型的最大地面速度（在静风条件下）。指定数值和计量单位。  - `maxLoad[number]`: 无人驾驶飞行器允许运输的最大负荷。指定数值和计量单位。  - `minUnladenWeight[number]`: 无人驾驶飞行器在充满燃料但无负载的情况下的重量。指定数值和计量单位。  - `minWeight[number]`: 无人驾驶飞行器的重量，不含燃料或负载。指定数值和计量单位。  - `model[string]`: 无人机模型标识符，可能是无人机模型。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `rotors[number]`: 无人驾驶飞行器模型的旋翼数量。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体标识符。它必须是UnmannedAerialVehicle。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
这个数据模型来自原始项目GSMA物联网项目，https://www.gsma.com/iot/iot-big-data/。有一些小的调整，以满足智能数据模型的要求。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicleModel:    
  description: 'This entity contains a harmonised description of a generic Unmanned Ariel Vehicle (UAV) model and is applicable to UAV command and control and related UAV transport applications.'    
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
    brandName:    
      description: 'A description of the brand name of this Unmanned Aerial Vehicle Model.'    
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
    documentation:    
      description: 'URI reference (URL/URN) to Product Data Sheet or other manufacturers documentation about this Unmanned Aerial Vehicle Model.'    
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
        - 'hybrid electric/petrol'    
        - 'hybrid electric/diesel'    
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
      anyOf: &unmannedaerialvehiclemodel_-_properties_-_owner_-_items_-_anyof    
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
    manufacturerName:    
      description: 'The name of the manufacturer of this Unmanned Aerial Vehicle Model.'    
      type: string    
      x-ngsi:    
        type: Property    
    maxFlightAltitude:    
      description: 'The maximum flight altitude of the Unmanned Aerial Vehicle Model above ground. Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    maxFlightTime:    
      description: 'The maximum duration of flight of the Unmanned Aerial Vehicle Model with full fuel and no load. Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    maxGroundVelocity:    
      description: 'The maximum ground velocity of the Unmanned Aerial Vehicle Model (under still wind conditions). Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    maxLoad:    
      description: 'The maximum load that the Unmanned Aerial Vehicle is permitted to transport. Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    minUnladenWeight:    
      description: 'The weight of the Unmanned Aerial Vehicle with full fuel but no load. Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    minWeight:    
      description: 'The weight of the Unmanned Aerial Vehicle without fuel or load. Specify value and units of measure.'    
      type: number    
      x-ngsi:    
        type: Property    
    model:    
      description: 'The UAV models identifier, which may be a Unmanned Aerial Vehicle Model.'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *unmannedaerialvehiclemodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    rotors:    
      description: 'The number of the rotors of the Unmanned Aerial Vehicle Model.'    
      type: number    
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
    type:    
      description: 'NGSI Entity identifier. It has to be UnmannedAerialVehicle'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ＃＃＃＃有效载荷的例子  
#### UnmannedAerialVehicleModel NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的UnmannedAerialVehicleModel的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### UnmannedAerialVehicleModel NGSI-v2 normalized Example  
下面是一个规范化的JSON-LD格式的UnmannedAerialVehicleModel的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
    "type": "Number",  
    "value": "gasoline"  
  },  
  "maxFlightTime": {  
    "type": "Number"  
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
#### UnmannedAerialVehicleModel NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的UnmannedAerialVehicleModel的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### UnmannedAerialVehicleModel NGSI-LD规范化实例  
这里是一个规范化的JSON-LD格式的UnmannedAerialVehicleModel的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
