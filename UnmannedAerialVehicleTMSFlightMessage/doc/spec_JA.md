エンティティです。UnmannedAerialVehicleTMSFlightMessage  
==============================================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMSFlightMessage/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、グローバルUTMアソシエーションプロトコルメッセージを含む、汎用のUAV UTMフライトメッセージの調和のとれた記述を含む。このエンティティは、主に無人航空機の制御と管理に関連している。各UnmannedAerialVehicleTMSFlightMessageインスタンスは、特定のUAVインスタンスに関連している**。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateObserved`: 注意：このフィールドはNGSIv2で使用するために定義され、現在は非推奨となっています。新しいエンティティやアプリケーションでは、**observedAt**と置き換えてください。  - `description`: このアイテムの説明  - `flightMessage`: JSONオブジェクトとしてエンコードされたGlobal UTM Messageとしてエンコードされた、現在のフライト状況を説明するフライトメッセージ https://bitbucket.org/global_utm/flight-declaration-protocol  - `id`: エンティティのユニークな識別子  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `name`: このアイテムの名前です。  - `observedAt`: UAVFlightMessageレコードの日付/時刻を示す。  - `originatedByUnmannedAutonomousVehicle`: メッセージの発信元を示す論理的な指標。真はUAV自身であることを示し、偽は別のソース、リスニングステーションのソフトウェアアプリケーション、または別のUAVであることを示す。  - `originator`: メッセージがUAVから直接発信されていない場合に、情報を報告した第三者のUAVインスタンスまたは他のエンティティ（例：リスニングステーション）を指す。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI Entity 識別子。UnmannedAerialVehicleTMSFlightMessageでなければならない。  - `unmannedAerialVehicle`: このUAVFlightMessageに関連するUAVエンティティへの参照。    
必須項目  
このデータモデルは、GSMAのIoTプロジェクト（https://www.gsma.com/iot/iot-big-data/）の原型となるものです。スマートデータモデルの要件を満たすために、いくつかのマイナーな調整が行われています。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicleTMSFlightMessage:    
  description: 'This entity contains a harmonised description of a generic UAV UTM Flight Message, which contains a Global UTM Association protocol message. This entity is primarily associated with the control and management of Unmanned Aerial Vehicles. Each UnmannedAerialVehicleTMSFlightMessage instance is related to a specific UAV instance.'    
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
    dateObserved:    
      description: 'Indicates the date/time the observation was recorded.Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **observedAt**'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
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
      anyOf: &unmannedaerialvehicletmsflightmessage_-_properties_-_owner_-_items_-_anyof    
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
    observedAt:    
      description: 'Indicates the date/time of the UAVFlightMessage record.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    originatedByUnmannedAutonomousVehicle:    
      description: 'A logical indicator of source of the message. True indicates it is the UAV itself, false indicates that it is a different source, a listening station software application or a different UAV.'    
      type: boolean    
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
      description: 'Refers to a third party UAV instance or other entity (e.g. listening station) that reported the information in the case the message was not directly originated by the UAV.'    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *unmannedaerialvehicletmsflightmessage_-_properties_-_owner_-_items_-_anyof    
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
    type:    
      description: 'NGSI Entity identifier. It has to be UnmannedAerialVehicleTMSFlightMessage'    
      enum:    
        - UnmannedAerialVehicleTMSFlightMessage    
      type: string    
      x-ngsi:    
        type: Property    
    unmannedAerialVehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the UAV entity to which this UAVFlightMessage relates.'    
      x-ngsi:    
        type: Relationship    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleTMSFlightMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMSFlightMessage/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### UnmannedAerialVehicleTMSFlightMessage NGSI-v2 key-values例  
UnmannedAerialVehicleTMSFlightMessageをkey-valuesとしてJSON-LD形式で表現した例を示します。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### UnmannedAerialVehicleTMSFlightMessage NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のUnmannedAerialVehicleTMSFlightMessageの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "type": "Relationship",  
    "object": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856"  
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
    "type": "Relationship",  
    "object": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec"  
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
#### UnmannedAerialVehicleTMSFlightMessage NGSI-LD key-values 例  
UnmannedAerialVehicleTMSFlightMessageをkey-valuesとしてJSON-LD形式で表現した例を示します。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMSFlightMessage/context.jsonld"  
  ]  
}  
```  
#### UnmannedAerialVehicleTMSFlightMessage NGSI-LD 正規化例  
ここでは、正規化されたJSON-LD形式のUnmannedAerialVehicleTMSFlightMessageの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleTMSFlightMessage/context.jsonld"  
  ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
