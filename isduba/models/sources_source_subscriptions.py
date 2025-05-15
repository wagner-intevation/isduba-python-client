# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sources_source_subscription import SourcesSourceSubscription


T = TypeVar("T", bound="SourcesSourceSubscriptions")


@_attrs_define
class SourcesSourceSubscriptions:
    """
    Attributes:
        available (Union[Unset, list[str]]):
        subscriptions (Union[Unset, list['SourcesSourceSubscription']]):
        url (Union[Unset, str]):
    """

    available: Union[Unset, list[str]] = UNSET
    subscriptions: Union[Unset, list["SourcesSourceSubscription"]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available: Union[Unset, list[str]] = UNSET
        if not isinstance(self.available, Unset):
            available = self.available

        subscriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_source_subscription import SourcesSourceSubscription

        d = dict(src_dict)
        available = cast(list[str], d.pop("available", UNSET))

        subscriptions = []
        _subscriptions = d.pop("subscriptions", UNSET)
        for subscriptions_item_data in _subscriptions or []:
            subscriptions_item = SourcesSourceSubscription.from_dict(subscriptions_item_data)

            subscriptions.append(subscriptions_item)

        url = d.pop("url", UNSET)

        sources_source_subscriptions = cls(
            available=available,
            subscriptions=subscriptions,
            url=url,
        )

        sources_source_subscriptions.additional_properties = d
        return sources_source_subscriptions

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
