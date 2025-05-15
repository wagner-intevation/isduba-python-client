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
    from ..models.web_feed_logs_entry import WebFeedLogsEntry


T = TypeVar("T", bound="WebFeedLogsFeedLogEntries")


@_attrs_define
class WebFeedLogsFeedLogEntries:
    """
    Attributes:
        count (Union[Unset, int]):
        entries (Union[Unset, list['WebFeedLogsEntry']]):
    """

    count: Union[Unset, int] = UNSET
    entries: Union[Unset, list["WebFeedLogsEntry"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_feed_logs_entry import WebFeedLogsEntry

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = WebFeedLogsEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        web_feed_logs_feed_log_entries = cls(
            count=count,
            entries=entries,
        )

        web_feed_logs_feed_log_entries.additional_properties = d
        return web_feed_logs_feed_log_entries

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
