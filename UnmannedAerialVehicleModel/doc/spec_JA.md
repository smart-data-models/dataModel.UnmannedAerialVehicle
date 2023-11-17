<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティUnmannedAerialVehicleModel (無人航空機モデル)    
===========================================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleModel/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**このエンティティは、一般的な無人航空機(UAV)モデルの調和された記述を含み、UAV の指揮制御および関連する UAV 輸送アプリケーションに適用される。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: この無人航空機モデルのブランド名の説明  - `categoryUAV[string]`: UAVModelの作業カテゴリ。空撮、植物保護、工業、経路検査、郵送、輸送' から選択します。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `documentation[string]`: この無人航空機モデルに関する製品データシートまたはその他のメーカーの文書へのURI参照（URL/URN）  - `fuelType[string]`: UAVModel を動かす燃料の種類。動力源を列挙したリストから選択します。Enum:'gasoline, petrol(unleaded), petrol(leaded), petrol, diesel, electric, hydrogen, lpg autogas, cng, biodiesel, ethanol, hybrid electric/petrol, hybrid electric/diesel, other'.  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `manufacturerName[string]`: この無人航空機モデルのメーカー名  - `maxFlightAltitude[number]`: 無人航空機モデルの地上からの最大飛行高度。値と単位を指定する  - `maxFlightTime[number]`: 燃料満タン、無負荷状態での無人航空機モデルの最大飛行時間。値と単位を指定する  - `maxGroundVelocity[number]`: 無人航空機モデルの最大対地速度（静止風条件下）。値と単位を指定する  - `maxLoad[number]`: 無人航空機が輸送を許可される最大積載量。値と単位を指定する  - `minUnladenWeight[number]`: 燃料を満タンにし、荷物を積んでいない状態の無人航空機の重量。値と単位を指定する  - `minWeight[number]`: 燃料や積載物を除いた無人航空機の重量。値と単位を指定する  - `model[string]`: UAVモデルの識別子は、無人航空機モデル（Unmanned Aerial Vehicle Model）であってもよい。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `rotors[number]`: 無人航空機モデルのローター数  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSI エンティティ識別子。これは UnmannedAerialVehicle でなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
このデータ・モデルはGSMA IoTプロジェクト（https://www.gsma.com/iot/iot-big-data/）に由来する。スマート・データ・モデルの要件を満たすために、若干の修正が加えられている。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### UnmannedAerialVehicleModel NGSI-v2 キー値の例    
JSON-LD形式のUnmannedAerialVehicleModelをkey-valuesとした例です。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### UnmannedAerialVehicleModel NGSI-v2 正規化例    
以下は、正規化された JSON-LD 形式の UnmannedAerialVehicleModel の例です。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト データを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVModel:6f4439d2-5925-11e8-a0ef-53719253dbbd",  
  "type": "UnmannedAerialVehicleModel",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "model": {  
    "type": "Text",  
    "value": "ACME Recon"  
  },  
  "documentation": {  
    "type": "Text",  
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
    "type": "Boolean",  
    "value": true  
  },  
  "minUnladenWeight": {  
    "type": "Number",  
    "value": 1.5  
  },  
  "maxLoad": {  
    "type": "Number",  
    "value": 0.8  
  }  
}  
```  
</details>    
#### UnmannedAerialVehicleModel NGSI-LD キー値の例    
JSON-LD形式のUnmannedAerialVehicleModelをkey-valuesとした例です。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### UnmannedAerialVehicleModel NGSI-LD 正規化例    
以下は、正規化された JSON-LD フォーマットの UnmannedAerialVehicleModel の例です。これは、オプションを使用しない場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
