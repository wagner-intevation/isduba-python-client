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
    from ..models.sources_feed_subscription import SourcesFeedSubscription


T = TypeVar("T", bound="SourcesSourceSubscription")


@_attrs_define
class SourcesSourceSubscription:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        subscripted (Union[Unset, list['SourcesFeedSubscription']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    subscripted: Union[Unset, list["SourcesFeedSubscription"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        subscripted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subscripted, Unset):
            subscripted = []
            for subscripted_item_data in self.subscripted:
                subscripted_item = subscripted_item_data.to_dict()
                subscripted.append(subscripted_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subscripted is not UNSET:
            field_dict["subscripted"] = subscripted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_feed_subscription import SourcesFeedSubscription

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        subscripted = []
        _subscripted = d.pop("subscripted", UNSET)
        for subscripted_item_data in _subscripted or []:
            subscripted_item = SourcesFeedSubscription.from_dict(subscripted_item_data)

            subscripted.append(subscripted_item)

        sources_source_subscription = cls(
            id=id,
            name=name,
            subscripted=subscripted,
        )

        sources_source_subscription.additional_properties = d
        return sources_source_subscription

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
