# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_duration import TimeDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebKeepFeedTimeKeepFeedTimeConfig")


@_attrs_define
class WebKeepFeedTimeKeepFeedTimeConfig:
    """
    Attributes:
        keep_feed_time (Union[Unset, TimeDuration]):
    """

    keep_feed_time: Union[Unset, TimeDuration] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keep_feed_time: Union[Unset, int] = UNSET
        if not isinstance(self.keep_feed_time, Unset):
            keep_feed_time = self.keep_feed_time.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keep_feed_time is not UNSET:
            field_dict["keep_feed_time"] = keep_feed_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _keep_feed_time = d.pop("keep_feed_time", UNSET)
        keep_feed_time: Union[Unset, TimeDuration]
        if isinstance(_keep_feed_time, Unset):
            keep_feed_time = UNSET
        else:
            keep_feed_time = TimeDuration(_keep_feed_time)

        web_keep_feed_time_keep_feed_time_config = cls(
            keep_feed_time=keep_feed_time,
        )

        web_keep_feed_time_keep_feed_time_config.additional_properties = d
        return web_keep_feed_time_keep_feed_time_config

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
