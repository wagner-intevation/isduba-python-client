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
    from ..models.web_custom import WebCustom


T = TypeVar("T", bound="WebArgumentedAggregator")


@_attrs_define
class WebArgumentedAggregator:
    """
    Attributes:
        aggregator (Union[Unset, list[int]]):
        custom (Union[Unset, WebCustom]):
    """

    aggregator: Union[Unset, list[int]] = UNSET
    custom: Union[Unset, "WebCustom"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregator: Union[Unset, list[int]] = UNSET
        if not isinstance(self.aggregator, Unset):
            aggregator = self.aggregator

        custom: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregator is not UNSET:
            field_dict["aggregator"] = aggregator
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_custom import WebCustom

        d = dict(src_dict)
        aggregator = cast(list[int], d.pop("aggregator", UNSET))

        _custom = d.pop("custom", UNSET)
        custom: Union[Unset, WebCustom]
        if isinstance(_custom, Unset):
            custom = UNSET
        else:
            custom = WebCustom.from_dict(_custom)

        web_argumented_aggregator = cls(
            aggregator=aggregator,
            custom=custom,
        )

        web_argumented_aggregator.additional_properties = d
        return web_argumented_aggregator

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
