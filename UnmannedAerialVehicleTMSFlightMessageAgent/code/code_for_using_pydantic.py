from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class OperationMode(Enum):
    vlos = 'vlos'
    evlos = 'evlos'
    bvlos = 'bvlos'
    automated = 'automated'


class FlightDeclaration(BaseModel):
    actualLandingTime: Optional[AwareDatetime] = Field(
        None, description='Actual landing time'
    )
    actualTakeOffTime: Optional[AwareDatetime] = Field(
        None, description='Actual take off time'
    )
    contactUrl: Optional[AnyUrl] = Field(
        None, description='A url for further information'
    )
    expectTelemetry: Optional[bool] = Field(
        None, description='Whether it is expected telemetry data '
    )
    idents: Optional[List[str]] = Field(
        None, description='Identifier items of the flight declaration'
    )
    operationMode: Optional[OperationMode] = Field(
        None, description='Operation mode of the flight'
    )
    originatingParty: Optional[str] = Field(
        None,
        description='Country from which the goods/items being transported originate.',
    )
    parts: Optional[List[str]] = Field(
        None,
        description='elements of the flight declaration that can include details about the operator, the aircraft, specific approvals, means of compliance, and continuing airworthiness management',
    )
    purpose: Optional[str] = Field(None, description='Purpose of the flight')


class FlightMessage(BaseModel):
    flightDeclaration: Optional[FlightDeclaration] = Field(
        None, description='Declaration of the flight'
    )
    flightId: Optional[str] = Field(None, description='Identifier of the flight')
    sequenceNumber: Optional[float] = Field(
        None, description='Index of the message in a sequence'
    )
    version: Optional[str] = Field(None, description='Version of the agent')


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    UnmannedAerialVehicleTMSFlightMessageAgent = (
        'UnmannedAerialVehicleTMSFlightMessageAgent'
    )


class UnmannedAerialVehicleTMSFlightMessageAgent(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    flightControlPolicy: Optional[str] = Field(
        None,
        description='Indicates the flight control policy generated by the service provider. This data could be included as a text value or referenced by a URI (URL/URN) to a policy defined in JSON or XML format',
    )
    flightMessage: Optional[FlightMessage] = Field(
        None,
        description='A flight message describing the current flight status encoded as a Global UTM Message encoded as a JSON object. https://bitbucket.org/global_utm/flight-declaration-protocol',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observedAt: Optional[AwareDatetime] = Field(
        None,
        description='Indicates the date/time of the UAVUTMFlightMessageAgent record',
    )
    originatedByUnmannedAutonomousVehicle: Optional[bool] = Field(
        None,
        description='A logical indicator of source of the message. True indicates it is the UAV itself, false indicates that it is a different source, a listening station software application or a different UAV',
    )
    originator: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Refers to a third party UAV instance or other entity (e.g. listening station) that reported the information in the case the message was not directly originated by the UAV',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None,
        description='NGSI Entity identifier. It has to be UnmannedAerialVehicleTMSFlightMessageAgent',
    )
    unmannedAerialVehicle: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the UAV entity to which this UAVUTMFlightMessageAgent relates',
    )
    validationResult: Optional[bool] = Field(
        None,
        description='A logical indicator of validation of the message. True indicates it is the validation is confirmed, false indicates that the validation confirmation fails',
    )