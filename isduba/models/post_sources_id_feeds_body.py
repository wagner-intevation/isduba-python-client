# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_sources_id_feeds_body_log_level import PostSourcesIdFeedsBodyLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSourcesIdFeedsBody")


@_attrs_define
class PostSourcesIdFeedsBody:
    """
    Attributes:
        label (str):
        url (str):
        log_level (Union[Unset, PostSourcesIdFeedsBodyLogLevel]):
        source_id (Union[Unset, int]):
    """

    label: str
    url: str
    log_level: Union[Unset, PostSourcesIdFeedsBodyLogLevel] = UNSET
    source_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        url = self.url

        log_level: Union[Unset, str] = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        source_id = self.source_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "url": url,
            }
        )
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if source_id is not UNSET:
            field_dict["sourceID"] = source_id

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        label = (None, str(self.label).encode(), "text/plain")

        url = (None, str(self.url).encode(), "text/plain")

        log_level: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = (None, str(self.log_level.value).encode(), "text/plain")

        source_id = (
            self.source_id if isinstance(self.source_id, Unset) else (None, str(self.source_id).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "label": label,
                "url": url,
            }
        )
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if source_id is not UNSET:
            field_dict["sourceID"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        url = d.pop("url")

        _log_level = d.pop("log_level", UNSET)
        log_level: Union[Unset, PostSourcesIdFeedsBodyLogLevel]
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = PostSourcesIdFeedsBodyLogLevel(_log_level)

        source_id = d.pop("sourceID", UNSET)

        post_sources_id_feeds_body = cls(
            label=label,
            url=url,
            log_level=log_level,
            source_id=source_id,
        )

        post_sources_id_feeds_body.additional_properties = d
        return post_sources_id_feeds_body

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
