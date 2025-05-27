# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebViewAggregatorsAggregator")


@_attrs_define
class WebViewAggregatorsAggregator:
    """
    Attributes:
        active (Union[Unset, bool]):
        attention (Union[Unset, bool]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    active: Union[Unset, bool] = UNSET
    attention: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        attention = self.attention

        id = self.id

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if attention is not UNSET:
            field_dict["attention"] = attention
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        attention = d.pop("attention", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        web_view_aggregators_aggregator = cls(
            active=active,
            attention=attention,
            id=id,
            name=name,
            url=url,
        )

        web_view_aggregators_aggregator.additional_properties = d
        return web_view_aggregators_aggregator

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
