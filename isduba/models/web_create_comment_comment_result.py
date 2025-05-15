# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_null_string import SqlNullString


T = TypeVar("T", bound="WebCreateCommentCommentResult")


@_attrs_define
class WebCreateCommentCommentResult:
    """
    Attributes:
        commentator (Union[Unset, SqlNullString]):
        id (Union[Unset, int]):
        time (Union[Unset, str]):
    """

    commentator: Union[Unset, "SqlNullString"] = UNSET
    id: Union[Unset, int] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commentator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.commentator, Unset):
            commentator = self.commentator.to_dict()

        id = self.id

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commentator is not UNSET:
            field_dict["commentator"] = commentator
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sql_null_string import SqlNullString

        d = dict(src_dict)
        _commentator = d.pop("commentator", UNSET)
        commentator: Union[Unset, SqlNullString]
        if isinstance(_commentator, Unset):
            commentator = UNSET
        else:
            commentator = SqlNullString.from_dict(_commentator)

        id = d.pop("id", UNSET)

        time = d.pop("time", UNSET)

        web_create_comment_comment_result = cls(
            commentator=commentator,
            id=id,
            time=time,
        )

        web_create_comment_comment_result.additional_properties = d
        return web_create_comment_comment_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
