# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebComment")


@_attrs_define
class WebComment:
    """
    Attributes:
        commentator (Union[Unset, str]):
        document_id (Union[Unset, int]):
        id (Union[Unset, int]):
        message (Union[Unset, str]):
        time (Union[Unset, str]):
    """

    commentator: Union[Unset, str] = UNSET
    document_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commentator = self.commentator

        document_id = self.document_id

        id = self.id

        message = self.message

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commentator is not UNSET:
            field_dict["commentator"] = commentator
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commentator = d.pop("commentator", UNSET)

        document_id = d.pop("document_id", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        time = d.pop("time", UNSET)

        web_comment = cls(
            commentator=commentator,
            document_id=document_id,
            id=id,
            message=message,
            time=time,
        )

        web_comment.additional_properties = d
        return web_comment

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
