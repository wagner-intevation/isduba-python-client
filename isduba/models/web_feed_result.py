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
    from ..models.web_feed import WebFeed


T = TypeVar("T", bound="WebFeedResult")


@_attrs_define
class WebFeedResult:
    """
    Attributes:
        feeds (Union[Unset, list['WebFeed']]):
    """

    feeds: Union[Unset, list["WebFeed"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feeds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.feeds, Unset):
            feeds = []
            for feeds_item_data in self.feeds:
                feeds_item = feeds_item_data.to_dict()
                feeds.append(feeds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feeds is not UNSET:
            field_dict["feeds"] = feeds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_feed import WebFeed

        d = dict(src_dict)
        feeds = []
        _feeds = d.pop("feeds", UNSET)
        for feeds_item_data in _feeds or []:
            feeds_item = WebFeed.from_dict(feeds_item_data)

            feeds.append(feeds_item)

        web_feed_result = cls(
            feeds=feeds,
        )

        web_feed_result.additional_properties = d
        return web_feed_result

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
