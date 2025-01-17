# generated by datamodel-codegen:
#   filename:  schema/type/entityHistory.json
#   timestamp: 2021-10-31T21:55:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field, confloat


class EntityVersionHistory(BaseModel):
    class Config:
        extra = Extra.forbid

    entityType: str = Field(
        ...,
        description='Entity type, such as `database`, `table`, `dashboard`, for which this version history is produced.',
    )
    versions: List


class EntityVersion(BaseModel):
    __root__: confloat(ge=0.1, multiple_of=0.1) = Field(
        ...,
        description='Metadata version of the entity in the form `Major.Minor`. First version always starts from `0.1` when the entity is created. When the backward compatible changes are made to the entity, only the `Minor` version is incremented - example `1.0` is changed to `1.1`. When backward incompatible changes are made the `Major` version is incremented - example `1.1` to `2.0`.',
    )


class ChangeDescription(BaseModel):
    class Config:
        extra = Extra.forbid

    fieldsAdded: Optional[List[str]] = Field(
        None, description='Fields added during the version changes.'
    )
    fieldsUpdated: Optional[List[str]] = Field(
        None, description='Fields modified during the version changes.'
    )
    fieldsDeleted: Optional[List[str]] = Field(
        None, description='Fields deleted during the version changes.'
    )
    previousVersion: Optional[EntityVersion] = None
