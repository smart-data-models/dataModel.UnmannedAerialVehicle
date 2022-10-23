<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : UnmannedAerialVehicle  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UnmannedAerialVehicle/blob/master/UnmannedAerialVehicle/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description harmonisée d'un véhicule aérien sans pilote (UAV) spécifique. Cette entité est principalement associée à la commande et au contrôle des UAV et aux applications connexes de transport d'UAV**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `UnmannedAerialVehicleModel[*]`: Référence à la définition du modèle de drone qui décrit le drone de manière plus détaillée.  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `elevation[number]`: L'élévation du drone (par rapport au niveau du sol à l'endroit spécifié). Précisez la valeur et les unités de mesure.  - `flightStatus[string]`: Le statut de vol du drone, y compris ceux-ci. Enum : 'stop, takeoff, flight, hover, land' (arrêt, décollage, vol, vol stationnaire, atterrissage)  - `fuel[number]`: Charge de carburant actuelle du drone. Spécifiez la valeur et les unités de mesure  - `groundSpeed[number]`: La dernière vitesse au sol signalée du drone. Spécifiez la valeur et les unités de mesure  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `observedAt[string]`: Indique la date/heure du dernier rapport de suivi ou de la dernière mise à jour.  - `operationMode[string]`: Texte décrivant le choix parmi ces valeurs. Enum : 'vlos, evlos, bvlos, automated'. Note : les descriptions s'alignent sur le message UTM Flight.  - `operator[array]`: Liste détaillant l'opérateur ou les opérateurs du drone. Renvoie à une ou plusieurs personnes ou organisations Schema.org.https://schema.org/Personhttps://schema.org/Organization  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Identifiant de l'entité NGSI. Il doit être UnmannedAerialVehicle.  - `workStatus[string]`: Le statut de travail du drone, y compris ceux-ci. Enum : 'stop, prepare, work, finish' (arrêter, préparer, travailler, terminer)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Ce modèle de données est issu du projet original GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Il y a quelques adaptations mineures pour répondre aux exigences des modèles de données intelligents.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UnmannedAerialVehicle:    
  description: 'This entity contains a harmonised description of a specific Unmanned Aerial Vehicle (UAV). This entity is primarily associated with UAV command and control and related UAV transport applications.'    
  properties:    
    UnmannedAerialVehicleModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the UAV Model definition which describes the UAV in more detail.'    
      x-ngsi:    
        type: Relationship    
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
    elevation:    
      description: 'The elevation of the UAV (relative to ground level at the specified location). Specify value and units of measure.'    
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
      description: 'Current fuel load of the UAV. Specify value and units of measure'    
      type: number    
      x-ngsi:    
        type: Property    
    groundSpeed:    
      description: 'The latest reported ground speed of the UAV. Specify value and units of measure'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &unmannedaerialvehicle_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Indicates the date/time of the latest monitoring report or update.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: 'Text describing the choice from these values. Enum:''vlos, evlos, bvlos, automated''. Note: descriptions align with UTM Flight message.'    
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
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *unmannedaerialvehicle_-_properties_-_owner_-_items_-_anyof    
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
      description: 'NGSI Entity identifier. It has to be UnmannedAerialVehicle'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## Exemples de charges utiles  
#### UnmannedAerialVehicle Valeurs clés NGSI-v2 Exemple  
Voici un exemple de UnmannedAerialVehicle au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### UnmannedAerialVehicle NGSI-v2 normalisé Exemple  
Voici un exemple d'un UnmannedAerialVehicle au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:UAV:1fa179a6-b507-4857-ad72-eb5513ef05c6",  
  "type": "UnmannedAerialVehicle",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "uavModel": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:UAVModel:23821045-33d4-46ec-b777-98f461bf4856"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Yellow1"  
  },  
  "owner": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Person:cdfd9cb8-ae2b-47cb-a43a-b9767ffd5c84",  
      "urn:ngsi-ld:Organization:1be9cd61-ef59-421f-a326-4b6c84411ad4"  
    ]  
  },  
  "operator": {  
    "type": "Relationship",  
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
#### UnmannedAerialVehicle Valeurs clés NGSI-LD Exemple  
Voici un exemple de UnmannedAerialVehicle au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### UnmannedAerialVehicle NGSI-LD normalisé Exemple  
Voici un exemple d'un UnmannedAerialVehicle au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
