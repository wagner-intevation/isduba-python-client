# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_feed_log_level import ConfigFeedLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebFeedLogsEntry")


@_attrs_define
class WebFeedLogsEntry:
    """
    Attributes:
        feed_id (Union[Unset, int]):
        level (Union[Unset, ConfigFeedLogLevel]):
        msg (Union[Unset, str]):
        time (Union[Unset, str]):
    """

    feed_id: Union[Unset, int] = UNSET
    level: Union[Unset, ConfigFeedLogLevel] = UNSET
    msg: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feed_id = self.feed_id

        level: Union[Unset, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        msg = self.msg

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feed_id is not UNSET:
            field_dict["feed_id"] = feed_id
        if level is not UNSET:
            field_dict["level"] = level
        if msg is not UNSET:
            field_dict["msg"] = msg
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feed_id = d.pop("feed_id", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, ConfigFeedLogLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = ConfigFeedLogLevel(_level)

        msg = d.pop("msg", UNSET)

        time = d.pop("time", UNSET)

        web_feed_logs_entry = cls(
            feed_id=feed_id,
            level=level,
            msg=msg,
            time=time,
        )

        web_feed_logs_entry.additional_properties = d
        return web_feed_logs_entry

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
