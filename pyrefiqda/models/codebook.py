from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

__NAMESPACE__ = "urn:QDA-XML:codebook:1.0"


class CodeType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
        },
    )
    code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
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


class MemberCodeType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    guid: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})",
        }
    )


class CodesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
            "min_occurs": 1,
        },
    )


class SetType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
        },
    )
    member_code: list[MemberCodeType] = field(
        default_factory=list,
        metadata={
            "name": "MemberCode",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
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


class SetsType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    set: list[SetType] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
            "min_occurs": 1,
        },
    )


class CodeBookType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    codes: CodesType = field(
        metadata={
            "name": "Codes",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
        }
    )
    sets: None | SetsType = field(
        default=None,
        metadata={
            "name": "Sets",
            "type": "Element",
            "namespace": "urn:QDA-XML:codebook:1.0",
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class CodeBook(CodeBookType):
    """
    This element MUST be conveyed as the root element in any instance
    document based on this Schema expression.
    """

    class Meta:
        namespace = "urn:QDA-XML:codebook:1.0"

    model_config = ConfigDict(defer_build=True)
