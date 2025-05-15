# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.web_overview_events_events_events_item_additional_property import (
        WebOverviewEventsEventsEventsItemAdditionalProperty,
    )


T = TypeVar("T", bound="WebOverviewEventsEventsEventsItem")


@_attrs_define
class WebOverviewEventsEventsEventsItem:
    """ """

    additional_properties: dict[str, "WebOverviewEventsEventsEventsItemAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_overview_events_events_events_item_additional_property import (
            WebOverviewEventsEventsEventsItemAdditionalProperty,
        )

        d = dict(src_dict)
        web_overview_events_events_events_item = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = WebOverviewEventsEventsEventsItemAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        web_overview_events_events_events_item.additional_properties = additional_properties
        return web_overview_events_events_events_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "WebOverviewEventsEventsEventsItemAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "WebOverviewEventsEventsEventsItemAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
