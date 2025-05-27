# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_sources_feeds_id_body_log_level import PutSourcesFeedsIdBodyLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutSourcesFeedsIdBody")


@_attrs_define
class PutSourcesFeedsIdBody:
    """
    Attributes:
        id (Union[Unset, int]):
        label (Union[Unset, str]):
        log_level (Union[Unset, PutSourcesFeedsIdBodyLogLevel]):
        rolie (Union[Unset, bool]):
        url (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    log_level: Union[Unset, PutSourcesFeedsIdBodyLogLevel] = UNSET
    rolie: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        log_level: Union[Unset, str] = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        rolie = self.rolie

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
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        log_level: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = (None, str(self.log_level.value).encode(), "text/plain")

        rolie = self.rolie if isinstance(self.rolie, Unset) else (None, str(self.rolie).encode(), "text/plain")

        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if rolie is not UNSET:
            field_dict["rolie"] = rolie
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        _log_level = d.pop("log_level", UNSET)
        log_level: Union[Unset, PutSourcesFeedsIdBodyLogLevel]
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = PutSourcesFeedsIdBodyLogLevel(_log_level)

        rolie = d.pop("rolie", UNSET)

        url = d.pop("url", UNSET)

        put_sources_feeds_id_body = cls(
            id=id,
            label=label,
            log_level=log_level,
            rolie=rolie,
            url=url,
        )

        put_sources_feeds_id_body.additional_properties = d
        return put_sources_feeds_id_body

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
