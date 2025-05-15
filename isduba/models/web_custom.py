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
    from ..models.sources_source_subscriptions import SourcesSourceSubscriptions


T = TypeVar("T", bound="WebCustom")


@_attrs_define
class WebCustom:
    """
    Attributes:
        attention (Union[Unset, bool]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        subscriptions (Union[Unset, list['SourcesSourceSubscriptions']]):
    """

    attention: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    subscriptions: Union[Unset, list["SourcesSourceSubscriptions"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention = self.attention

        id = self.id

        name = self.name

        subscriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attention is not UNSET:
            field_dict["attention"] = attention
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_source_subscriptions import SourcesSourceSubscriptions

        d = dict(src_dict)
        attention = d.pop("attention", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        subscriptions = []
        _subscriptions = d.pop("subscriptions", UNSET)
        for subscriptions_item_data in _subscriptions or []:
            subscriptions_item = SourcesSourceSubscriptions.from_dict(subscriptions_item_data)

            subscriptions.append(subscriptions_item)

        web_custom = cls(
            attention=attention,
            id=id,
            name=name,
            subscriptions=subscriptions,
        )

        web_custom.additional_properties = d
        return web_custom

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
