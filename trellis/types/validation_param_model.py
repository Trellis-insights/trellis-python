# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ValidationParamModel(pydantic.BaseModel):
    """
    Represents a validation parameter in the system.

    Attributes:
    id (str): The ID of the validation parameter.
    transform_id (str): The ID of the associated transform.
    validation_name (str | None): The name of the validation.
    validation_rule (str | None): The rule for the validation.
    validation_columns (List[str] | None): The list of columns to be validated.
    """

    created_at: typing.Optional[dt.datetime]
    updated_at: typing.Optional[dt.datetime]
    id: typing.Optional[str]
    transform_id: str
    validation_name: typing.Optional[str]
    validation_rule: typing.Optional[str]
    validation_columns: typing.Optional[typing.List[str]]
    deleted_at: typing.Optional[dt.datetime]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}