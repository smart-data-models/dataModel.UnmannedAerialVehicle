<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Véhicules aériens sans pilote (DASB)    
=============================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleADSB/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité contient une description harmonisée d'une diffusion générique de surveillance dépendante automatique de véhicules aériens sans pilote (UAV). Cette entité est principalement associée au contrôle et à la gestion des véhicules aériens sans pilote. Chaque instance d'UAVADSB sera liée à une instance d'UAV spécifique**.    
version : 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `UnmannedAerialVehicle[*]`: Référence à l'entité du véhicule aérien sans pilote à laquelle ce message de diffusion se rapporte  - `UnmannedAerialVehicleADSBroadcast[string]`: Message de vol décrivant l'état actuel du vol en tant que message DBSB stocké sous la forme d'une chaîne de chiffres hexadécimaux.  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `observedAt[date-time]`: Indique la date et l'heure de la diffusion DBS  - `originatedByUnmannedAerialVehicle[boolean]`: Indicateur logique de la source du message. True indique qu'il s'agit du drone lui-même, false indique qu'il s'agit d'une source différente, d'une application logicielle d'une station d'écoute ou d'un drone différent.  - `originator[*]`: Désigne une instance de drone tierce ou une autre entité (par exemple une station d'écoute) qui a communiqué l'information dans le cas où le message n'émane pas directement du drone.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Identifiant de l'entité NGSI. Il doit s'agir de UnmannedAerialVehicleADSB.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Ce modèle de données provient du projet original GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Il a fait l'objet de quelques adaptations mineures pour répondre aux exigences des modèles de données intelligents.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
UnmannedAerialVehicleADSB:      
  description: This entity contains a harmonised description of a generic UnmannedAerialVehicle (UAV) Automatic Dependent Surveillance–Broadcast. This entity is primarily associated with the control and management of Unmanned Aerial Vehicles. Each UAVADSB instance will be related to a specific UAV instance.      
  properties:      
    UnmannedAerialVehicle:      
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
      description: Reference to the Unmanned Aerial Vehicle entity to which this broadcast message relates      
      x-ngsi:      
        type: Relationship      
    UnmannedAerialVehicleADSBroadcast:      
      description: A flight message describing the current flight status as a DBSB Message stored as a string of hexadecimal digits      
      type: string      
      x-ngsi:      
        type: Property      
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
    observedAt:      
      description: Indicates the date/time of the DBS broadcast      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    originatedByUnmannedAerialVehicle:      
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
      description: NGSI Entity identifier. It has to be UnmannedAerialVehicleADSB      
      enum:      
        - UnmannedAerialVehicleADSB      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicleADSB/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UnmannedAerialVehicle/UnmannedAerialVehicleADSB/schema.json      
  x-model-tags: GSMA      
  x-version: 0.1.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### UnmannedAerialVehicleADSB Valeurs clés de l'INSIG-v2 Exemple    
Voici un exemple de UnmannedAerialVehicleADSB au format JSON-LD en tant que valeurs clés. Ceci est compatible avec la NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVADSB:1fa179a6-b507-4857-ad72-eb5513ef05c8",  
  "type": "UnmannedAerialVehicleADSB",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "unmannedAutonomousVehicle": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "observedAt": "2016-08-23T10:18:16Z",  
  "originatedByUnmannedAutonomousVehicle": false,  
  "originator": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec",  
  "UnmannedAutonomousVehicleADSBroadcast": "8D4840D6202CC371C32CE0576098"  
}  
```  
</details>    
#### UnmannedAerialVehicleADSB NGSI-v2 normalisé Exemple    
Voici un exemple de UnmannedAerialVehicleADSB au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:UAVADSB:1fa179a6-b507-4857-ad72-eb5513ef05c8",  
  "type": "UnmannedAerialVehicleADSB",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "unmannedAutonomousVehicle": {  
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
  "UnmannedAutonomousVehicleADSBroadcast": {  
    "type": "Text",  
    "value": "8D4840D6202CC371C32CE0576098"  
  }  
}  
```  
</details>    
#### UnmannedAerialVehicleADSB Valeurs clés de la NGSI-LD Exemple    
Voici un exemple de UnmannedAerialVehicleADSB au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.UnmannedAutonomousVehicle/UnmannedAutonomousVehicleADSB/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:UAVADSB:1fa179a6-b507-4857-ad72-eb5513ef05c8",  
  "type": "UnmannedAerialVehicleADSB",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "unmannedAutonomousVehicle": "urn:ngsi-ld:UAV:23821045-33d4-46ec-b777-98f461bf4856",  
  "observedAt": "2016-08-23T10:18:16Z",  
  "originatedByUnmannedAutonomousVehicle": false,  
  "originator": "urn:ngsi-ld:UAV:29935bbe-5922-11e8-9742-93bfb84686ec",  
  "UnmannedAutonomousVehicleADSBroadcast": "8D4840D6202CC371C32CE0576098"  
}  
```  
</details>    
#### UnmannedAerialVehicleADSB NGSI-LD normalisé Exemple    
Voici un exemple de UnmannedAerialVehicleADSB au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.UnmannedAutonomousVehicle/UnmannedAutonomousVehicleADSB/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UnmannedAerialVehicle/master/context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:UAVADSB:1fa179a6-b507-4857-ad72-eb5513ef05c8",  
    "type": "UnmannedAerialVehicleADSB",  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "unmannedAutonomousVehicle": {  
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
    "UnmannedAutonomousVehicleADSBroadcast": {  
        "type": "Property",  
        "value": "8D4840D6202CC371C32CE0576098"  
    }  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
