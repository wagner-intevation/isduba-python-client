# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutAggregatorsIdBody")


@_attrs_define
class PutAggregatorsIdBody:
    """
    Attributes:
        name (Union[Unset, str]): Aggregator name
        url (Union[Unset, str]): Aggregator URL
        active (Union[Unset, bool]): Aggregator active flag
        attention (Union[Unset, bool]): Aggregator attention flag
    """

    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    attention: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        active = self.active

        attention = self.attention

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if active is not UNSET:
            field_dict["active"] = active
        if attention is not UNSET:
            field_dict["attention"] = attention

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")

        active = self.active if isinstance(self.active, Unset) else (None, str(self.active).encode(), "text/plain")

        attention = (
            self.attention if isinstance(self.attention, Unset) else (None, str(self.attention).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if active is not UNSET:
            field_dict["active"] = active
        if attention is not UNSET:
            field_dict["attention"] = attention

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        active = d.pop("active", UNSET)

        attention = d.pop("attention", UNSET)

        put_aggregators_id_body = cls(
            name=name,
            url=url,
            active=active,
            attention=attention,
        )

        put_aggregators_id_body.additional_properties = d
        return put_aggregators_id_body

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
