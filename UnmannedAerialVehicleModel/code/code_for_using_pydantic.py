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


class CategoryUAV(Enum):
    aerialPhotography = 'aerialPhotography'
    industry = 'industry'
    mailing = 'mailing'
    plantProtection = 'plantProtection'
    routingInspection = 'routingInspection'
    transportation = 'transportation'


class FuelType(Enum):
    biodiesel = 'biodiesel'
    cng = 'cng'
    diesel = 'diesel'
    electric = 'electric'
    ethanol = 'ethanol'
    gasoline = 'gasoline'
    hybrid_electric_petrol = 'hybrid electric/petrol'
    hybrid_electric_diesel = 'hybrid electric/diesel'
    hydrogen = 'hydrogen'
    lpgAutogas = 'lpgAutogas'
    other = 'other'
    petrol = 'petrol'
    petrol_unleaded_ = 'petrol(unleaded)'
    petrol_leaded_ = 'petrol(leaded)'


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
    UnmannedAerialVehicleModel = 'UnmannedAerialVehicleModel'


class UnmannedAerialVehicleModel(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    brandName: Optional[str] = Field(
        None,
        description='A description of the brand name of this Unmanned Aerial Vehicle Model',
    )
    categoryUAV: Optional[CategoryUAV] = Field(
        None,
        description="The work category of the UAVModel. A choice from the following listnum:'aerialPhotography, plantProtection, industry, routingInspection, mailing, transportation'",
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
    documentation: Optional[str] = Field(
        None,
        description='URI reference (URL/URN) to Product Data Sheet or other manufacturers documentation about this Unmanned Aerial Vehicle Model',
    )
    fuelType: Optional[FuelType] = Field(
        None,
        description="The fuel type powering the UAVModel. A choice from an enumerated list describing the power source. Enum:'gasoline, petrol(unleaded), petrol(leaded), petrol, diesel, electric, hydrogen, lpg autogas, cng, biodiesel, ethanol, hybrid electric/petrol, hybrid electric/diesel, other'",
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
    manufacturerName: Optional[str] = Field(
        None,
        description='The name of the manufacturer of this Unmanned Aerial Vehicle Model',
    )
    maxFlightAltitude: Optional[float] = Field(
        None,
        description='The maximum flight altitude of the Unmanned Aerial Vehicle Model above ground. Specify value and units of measure',
    )
    maxFlightTime: Optional[float] = Field(
        None,
        description='The maximum duration of flight of the Unmanned Aerial Vehicle Model with full fuel and no load. Specify value and units of measure',
    )
    maxGroundVelocity: Optional[float] = Field(
        None,
        description='The maximum ground velocity of the Unmanned Aerial Vehicle Model (under still wind conditions). Specify value and units of measure',
    )
    maxLoad: Optional[float] = Field(
        None,
        description='The maximum load that the Unmanned Aerial Vehicle is permitted to transport. Specify value and units of measure',
    )
    minUnladenWeight: Optional[float] = Field(
        None,
        description='The weight of the Unmanned Aerial Vehicle with full fuel but no load. Specify value and units of measure',
    )
    minWeight: Optional[float] = Field(
        None,
        description='The weight of the Unmanned Aerial Vehicle without fuel or load. Specify value and units of measure',
    )
    model: Optional[str] = Field(
        None,
        description='The UAV models identifier, which may be a Unmanned Aerial Vehicle Model',
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    rotors: Optional[float] = Field(
        None,
        description='The number of the rotors of the Unmanned Aerial Vehicle Model',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity identifier. It has to be UnmannedAerialVehicle'
    )
