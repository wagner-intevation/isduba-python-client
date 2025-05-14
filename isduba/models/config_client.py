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

T = TypeVar("T", bound="ConfigClient")


@_attrs_define
class ConfigClient:
    """
    Attributes:
        idle_timeout (Union[Unset, TimeDuration]):
        keycloak_client_id (Union[Unset, str]):
        keycloak_realm (Union[Unset, str]):
        keycloak_url (Union[Unset, str]):
        update_interval (Union[Unset, TimeDuration]):
    """

    idle_timeout: Union[Unset, TimeDuration] = UNSET
    keycloak_client_id: Union[Unset, str] = UNSET
    keycloak_realm: Union[Unset, str] = UNSET
    keycloak_url: Union[Unset, str] = UNSET
    update_interval: Union[Unset, TimeDuration] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idle_timeout: Union[Unset, int] = UNSET
        if not isinstance(self.idle_timeout, Unset):
            idle_timeout = self.idle_timeout.value

        keycloak_client_id = self.keycloak_client_id

        keycloak_realm = self.keycloak_realm

        keycloak_url = self.keycloak_url

        update_interval: Union[Unset, int] = UNSET
        if not isinstance(self.update_interval, Unset):
            update_interval = self.update_interval.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idle_timeout is not UNSET:
            field_dict["idle_timeout"] = idle_timeout
        if keycloak_client_id is not UNSET:
            field_dict["keycloak_client_id"] = keycloak_client_id
        if keycloak_realm is not UNSET:
            field_dict["keycloak_realm"] = keycloak_realm
        if keycloak_url is not UNSET:
            field_dict["keycloak_url"] = keycloak_url
        if update_interval is not UNSET:
            field_dict["update_interval"] = update_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _idle_timeout = d.pop("idle_timeout", UNSET)
        idle_timeout: Union[Unset, TimeDuration]
        if isinstance(_idle_timeout, Unset):
            idle_timeout = UNSET
        else:
            idle_timeout = TimeDuration(_idle_timeout)

        keycloak_client_id = d.pop("keycloak_client_id", UNSET)

        keycloak_realm = d.pop("keycloak_realm", UNSET)

        keycloak_url = d.pop("keycloak_url", UNSET)

        _update_interval = d.pop("update_interval", UNSET)
        update_interval: Union[Unset, TimeDuration]
        if isinstance(_update_interval, Unset):
            update_interval = UNSET
        else:
            update_interval = TimeDuration(_update_interval)

        config_client = cls(
            idle_timeout=idle_timeout,
            keycloak_client_id=keycloak_client_id,
            keycloak_realm=keycloak_realm,
            keycloak_url=keycloak_url,
            update_interval=update_interval,
        )

        config_client.additional_properties = d
        return config_client

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
