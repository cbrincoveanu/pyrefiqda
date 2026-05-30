from __future__ import annotations

from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "urn:QDA-XML:project:1.0"


class CodeRefType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_guid: str = field(
        metadata={
            "name": "targetGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )


class LineStyleType(Enum):
    DOTTED = "dotted"
    DASHED = "dashed"
    SOLID = "solid"


class NoteRefType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_guid: str = field(
        metadata={
            "name": "targetGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )


class SelectionRefType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_guid: str = field(
        metadata={
            "name": "targetGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )


class ShapeType(Enum):
    PERSON = "Person"
    OVAL = "Oval"
    RECTANGLE = "Rectangle"
    ROUNDED_RECTANGLE = "RoundedRectangle"
    STAR = "Star"
    LEFT_TRIANGLE = "LeftTriangle"
    RIGHT_TRIANGLE = "RightTriangle"
    UP_TRIANGLE = "UpTriangle"
    DOWN_TRIANGLE = "DownTriangle"
    NOTE = "Note"


class SourceRefType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_guid: str = field(
        metadata={
            "name": "targetGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )


class SyncPointType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    time_stamp: None | int = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
        },
    )
    position: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class UserType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class VariableRefType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    target_guid: str = field(
        metadata={
            "name": "targetGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )


class DirectionType(Enum):
    ASSOCIATIVE = "Associative"
    ONE_WAY = "OneWay"
    BIDIRECTIONAL = "Bidirectional"


class TypeOfVariableType(Enum):
    TEXT = "Text"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
    FLOAT = "Float"
    DATE = "Date"
    DATE_TIME = "DateTime"


class CodeType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    is_codable: bool = field(
        metadata={
            "name": "isCodable",
            "type": "Attribute",
        }
    )
    color: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})",
        },
    )


class CodingType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code_ref: CodeRefType = field(
        metadata={
            "name": "CodeRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        }
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )


class EdgeType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    represented_guid: None | str = field(
        default=None,
        metadata={
            "name": "representedGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    source_vertex: str = field(
        metadata={
            "name": "sourceVertex",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    target_vertex: str = field(
        metadata={
            "name": "targetVertex",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    color: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})",
        },
    )
    direction: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    line_style: None | LineStyleType = field(
        default=None,
        metadata={
            "name": "lineStyle",
            "type": "Attribute",
        },
    )


class LinkType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    direction: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    color: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})",
        },
    )
    origin_guid: None | str = field(
        default=None,
        metadata={
            "name": "originGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    target_guid: None | str = field(
        default=None,
        metadata={
            "name": "targetGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )


class SetType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    member_code: list[CodeRefType] = field(
        default_factory=list,
        metadata={
            "name": "MemberCode",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    member_source: list[SourceRefType] = field(
        default_factory=list,
        metadata={
            "name": "MemberSource",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    member_note: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "MemberNote",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )


class UsersType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    user: list[UserType] = field(
        default_factory=list,
        metadata={
            "name": "User",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class VariableType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    type_of_variable: TypeOfVariableType = field(
        metadata={
            "name": "typeOfVariable",
            "type": "Attribute",
        }
    )


class VariableValueType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    variable_ref: VariableRefType = field(
        metadata={
            "name": "VariableRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        }
    )
    text_value: None | str = field(
        default=None,
        metadata={
            "name": "TextValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    boolean_value: None | bool = field(
        default=None,
        metadata={
            "name": "BooleanValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    integer_value: None | int = field(
        default=None,
        metadata={
            "name": "IntegerValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    float_value: None | Decimal = field(
        default=None,
        metadata={
            "name": "FloatValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    date_value: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DateValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    date_time_value: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DateTimeValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )


class VertexType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    represented_guid: None | str = field(
        default=None,
        metadata={
            "name": "representedGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    first_x: int = field(
        metadata={
            "name": "firstX",
            "type": "Attribute",
        }
    )
    first_y: int = field(
        metadata={
            "name": "firstY",
            "type": "Attribute",
        }
    )
    second_x: None | int = field(
        default=None,
        metadata={
            "name": "secondX",
            "type": "Attribute",
        },
    )
    second_y: None | int = field(
        default=None,
        metadata={
            "name": "secondY",
            "type": "Attribute",
        },
    )
    shape: None | ShapeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    color: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})",
        },
    )


class AudioSelectionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    begin: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    end: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class CaseType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    code_ref: list[CodeRefType] = field(
        default_factory=list,
        metadata={
            "name": "CodeRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "name": "VariableValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    source_ref: list[SourceRefType] = field(
        default_factory=list,
        metadata={
            "name": "SourceRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    selection_ref: list[SelectionRefType] = field(
        default_factory=list,
        metadata={
            "name": "SelectionRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class CodesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class GraphType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    vertex: list[VertexType] = field(
        default_factory=list,
        metadata={
            "name": "Vertex",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    edge: list[EdgeType] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class LinksType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: list[LinkType] = field(
        default_factory=list,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class PictureSelectionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    first_x: int = field(
        metadata={
            "name": "firstX",
            "type": "Attribute",
        }
    )
    first_y: int = field(
        metadata={
            "name": "firstY",
            "type": "Attribute",
        }
    )
    second_x: int = field(
        metadata={
            "name": "secondX",
            "type": "Attribute",
        }
    )
    second_y: int = field(
        metadata={
            "name": "secondY",
            "type": "Attribute",
        }
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class PlainTextSelectionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    start_position: int = field(
        metadata={
            "name": "startPosition",
            "type": "Attribute",
        }
    )
    end_position: int = field(
        metadata={
            "name": "endPosition",
            "type": "Attribute",
        }
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class SetsType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    set: list[SetType] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class TranscriptSelectionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    from_sync_point: None | str = field(
        default=None,
        metadata={
            "name": "fromSyncPoint",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    to_sync_point: None | str = field(
        default=None,
        metadata={
            "name": "toSyncPoint",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class VariablesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    variable: list[VariableType] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class VideoSelectionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    begin: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    end: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class CasesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    case: list[CaseType] = field(
        default_factory=list,
        metadata={
            "name": "Case",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class CodeBookType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    codes: CodesType = field(
        metadata={
            "name": "Codes",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        }
    )


class GraphsType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    graph: list[GraphType] = field(
        default_factory=list,
        metadata={
            "name": "Graph",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class TextSourceType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    plain_text_content: None | str = field(
        default=None,
        metadata={
            "name": "PlainTextContent",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    plain_text_selection: list[PlainTextSelectionType] = field(
        default_factory=list,
        metadata={
            "name": "PlainTextSelection",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "name": "VariableValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rich_text_path: None | str = field(
        default=None,
        metadata={
            "name": "richTextPath",
            "type": "Attribute",
        },
    )
    plain_text_path: None | str = field(
        default=None,
        metadata={
            "name": "plainTextPath",
            "type": "Attribute",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class TranscriptType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    plain_text_content: None | str = field(
        default=None,
        metadata={
            "name": "PlainTextContent",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    sync_point: list[SyncPointType] = field(
        default_factory=list,
        metadata={
            "name": "SyncPoint",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    transcript_selection: list[TranscriptSelectionType] = field(
        default_factory=list,
        metadata={
            "name": "TranscriptSelection",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rich_text_path: None | str = field(
        default=None,
        metadata={
            "name": "richTextPath",
            "type": "Attribute",
        },
    )
    plain_text_path: None | str = field(
        default=None,
        metadata={
            "name": "plainTextPath",
            "type": "Attribute",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class AudioSourceType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    transcript: list[TranscriptType] = field(
        default_factory=list,
        metadata={
            "name": "Transcript",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    audio_selection: list[AudioSelectionType] = field(
        default_factory=list,
        metadata={
            "name": "AudioSelection",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "name": "VariableValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    current_path: None | str = field(
        default=None,
        metadata={
            "name": "currentPath",
            "type": "Attribute",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class NotesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    note: list[TextSourceType] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
            "min_occurs": 1,
        },
    )


class PdfselectionType(BaseModel):
    class Meta:
        name = "PDFSelectionType"

    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    representation: None | TextSourceType = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    page: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    first_x: int = field(
        metadata={
            "name": "firstX",
            "type": "Attribute",
        }
    )
    first_y: int = field(
        metadata={
            "name": "firstY",
            "type": "Attribute",
        }
    )
    second_x: int = field(
        metadata={
            "name": "secondX",
            "type": "Attribute",
        }
    )
    second_y: int = field(
        metadata={
            "name": "secondY",
            "type": "Attribute",
        }
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class PictureSourceType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    text_description: None | TextSourceType = field(
        default=None,
        metadata={
            "name": "TextDescription",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    picture_selection: list[PictureSelectionType] = field(
        default_factory=list,
        metadata={
            "name": "PictureSelection",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "name": "VariableValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    current_path: None | str = field(
        default=None,
        metadata={
            "name": "currentPath",
            "type": "Attribute",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class VideoSourceType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    transcript: list[TranscriptType] = field(
        default_factory=list,
        metadata={
            "name": "Transcript",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    video_selection: list[VideoSelectionType] = field(
        default_factory=list,
        metadata={
            "name": "VideoSelection",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "name": "VariableValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    current_path: None | str = field(
        default=None,
        metadata={
            "name": "currentPath",
            "type": "Attribute",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class PdfsourceType(BaseModel):
    class Meta:
        name = "PDFSourceType"

    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    pdfselection: list[PdfselectionType] = field(
        default_factory=list,
        metadata={
            "name": "PDFSelection",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    representation: None | TextSourceType = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    coding: list[CodingType] = field(
        default_factory=list,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "name": "VariableValue",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    current_path: None | str = field(
        default=None,
        metadata={
            "name": "currentPath",
            "type": "Attribute",
        },
    )
    creating_user: None | str = field(
        default=None,
        metadata={
            "name": "creatingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUser",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )


class SourcesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_source: list[TextSourceType] = field(
        default_factory=list,
        metadata={
            "name": "TextSource",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    picture_source: list[PictureSourceType] = field(
        default_factory=list,
        metadata={
            "name": "PictureSource",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    pdfsource: list[PdfsourceType] = field(
        default_factory=list,
        metadata={
            "name": "PDFSource",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    audio_source: list[AudioSourceType] = field(
        default_factory=list,
        metadata={
            "name": "AudioSource",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    video_source: list[VideoSourceType] = field(
        default_factory=list,
        metadata={
            "name": "VideoSource",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )


class ProjectType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    users: None | UsersType = field(
        default=None,
        metadata={
            "name": "Users",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    code_book: None | CodeBookType = field(
        default=None,
        metadata={
            "name": "CodeBook",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    variables: None | VariablesType = field(
        default=None,
        metadata={
            "name": "Variables",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    cases: None | CasesType = field(
        default=None,
        metadata={
            "name": "Cases",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    sources: None | SourcesType = field(
        default=None,
        metadata={
            "name": "Sources",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    notes: None | NotesType = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    links: None | LinksType = field(
        default=None,
        metadata={
            "name": "Links",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    sets: None | SetsType = field(
        default=None,
        metadata={
            "name": "Sets",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    graphs: None | GraphsType = field(
        default=None,
        metadata={
            "name": "Graphs",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    note_ref: list[NoteRefType] = field(
        default_factory=list,
        metadata={
            "name": "NoteRef",
            "type": "Element",
            "namespace": "urn:QDA-XML:project:1.0",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    creating_user_guid: None | str = field(
        default=None,
        metadata={
            "name": "creatingUserGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    creation_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDateTime",
            "type": "Attribute",
        },
    )
    modifying_user_guid: None | str = field(
        default=None,
        metadata={
            "name": "modifyingUserGUID",
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        },
    )
    modified_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "modifiedDateTime",
            "type": "Attribute",
        },
    )
    base_path: None | str = field(
        default=None,
        metadata={
            "name": "basePath",
            "type": "Attribute",
        },
    )


class Project(ProjectType):
    """
    This element MUST be conveyed as the root element in any instance
    document based on this Schema expression.
    """

    class Meta:
        namespace = "urn:QDA-XML:project:1.0"

    model_config = ConfigDict(defer_build=True)
