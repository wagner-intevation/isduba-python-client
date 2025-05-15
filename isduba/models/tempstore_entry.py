# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TempstoreEntry")


@_attrs_define
class TempstoreEntry:
    """
    Attributes:
        expired (Union[Unset, str]):
        filename (Union[Unset, str]):
        id (Union[Unset, int]):
        inserted (Union[Unset, str]):
        length (Union[Unset, int]):
    """

    expired: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    inserted: Union[Unset, str] = UNSET
    length: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expired = self.expired

        filename = self.filename

        id = self.id

        inserted = self.inserted

        length = self.length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expired is not UNSET:
            field_dict["expired"] = expired
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if inserted is not UNSET:
            field_dict["inserted"] = inserted
        if length is not UNSET:
            field_dict["length"] = length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expired = d.pop("expired", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        inserted = d.pop("inserted", UNSET)

        length = d.pop("length", UNSET)

        tempstore_entry = cls(
            expired=expired,
            filename=filename,
            id=id,
            inserted=inserted,
            length=length,
        )

        tempstore_entry.additional_properties = d
        return tempstore_entry

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
