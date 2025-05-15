# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_feed_log_level import ConfigFeedLogLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sources_stats import SourcesStats


T = TypeVar("T", bound="WebFeed")


@_attrs_define
class WebFeed:
    """
    Attributes:
        id (Union[Unset, int]):
        label (Union[Unset, str]):
        log_level (Union[Unset, ConfigFeedLogLevel]):
        rolie (Union[Unset, bool]):
        stats (Union[Unset, SourcesStats]):
        url (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    log_level: Union[Unset, ConfigFeedLogLevel] = UNSET
    rolie: Union[Unset, bool] = UNSET
    stats: Union[Unset, "SourcesStats"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        log_level: Union[Unset, int] = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        rolie = self.rolie

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if rolie is not UNSET:
            field_dict["rolie"] = rolie
        if stats is not UNSET:
            field_dict["stats"] = stats
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_stats import SourcesStats

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        _log_level = d.pop("log_level", UNSET)
        log_level: Union[Unset, ConfigFeedLogLevel]
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = ConfigFeedLogLevel(_log_level)

        rolie = d.pop("rolie", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, SourcesStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = SourcesStats.from_dict(_stats)

        url = d.pop("url", UNSET)

        web_feed = cls(
            id=id,
            label=label,
            log_level=log_level,
            rolie=rolie,
            stats=stats,
            url=url,
        )

        web_feed.additional_properties = d
        return web_feed

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
