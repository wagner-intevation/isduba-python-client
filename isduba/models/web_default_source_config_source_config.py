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
    from ..models.web_source_age import WebSourceAge


T = TypeVar("T", bound="WebDefaultSourceConfigSourceConfig")


@_attrs_define
class WebDefaultSourceConfigSourceConfig:
    """
    Attributes:
        age (Union[Unset, WebSourceAge]):
        log_level (Union[Unset, ConfigFeedLogLevel]):
        rate (Union[Unset, float]):
        secure (Union[Unset, bool]):
        signature_check (Union[Unset, bool]):
        slots (Union[Unset, int]):
        strict_mode (Union[Unset, bool]):
    """

    age: Union[Unset, "WebSourceAge"] = UNSET
    log_level: Union[Unset, ConfigFeedLogLevel] = UNSET
    rate: Union[Unset, float] = UNSET
    secure: Union[Unset, bool] = UNSET
    signature_check: Union[Unset, bool] = UNSET
    slots: Union[Unset, int] = UNSET
    strict_mode: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.age, Unset):
            age = self.age.to_dict()

        log_level: Union[Unset, int] = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        rate = self.rate

        secure = self.secure

        signature_check = self.signature_check

        slots = self.slots

        strict_mode = self.strict_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age is not UNSET:
            field_dict["age"] = age
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if rate is not UNSET:
            field_dict["rate"] = rate
        if secure is not UNSET:
            field_dict["secure"] = secure
        if signature_check is not UNSET:
            field_dict["signature_check"] = signature_check
        if slots is not UNSET:
            field_dict["slots"] = slots
        if strict_mode is not UNSET:
            field_dict["strict_mode"] = strict_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_source_age import WebSourceAge

        d = dict(src_dict)
        _age = d.pop("age", UNSET)
        age: Union[Unset, WebSourceAge]
        if isinstance(_age, Unset):
            age = UNSET
        else:
            age = WebSourceAge.from_dict(_age)

        _log_level = d.pop("log_level", UNSET)
        log_level: Union[Unset, ConfigFeedLogLevel]
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = ConfigFeedLogLevel(_log_level)

        rate = d.pop("rate", UNSET)

        secure = d.pop("secure", UNSET)

        signature_check = d.pop("signature_check", UNSET)

        slots = d.pop("slots", UNSET)

        strict_mode = d.pop("strict_mode", UNSET)

        web_default_source_config_source_config = cls(
            age=age,
            log_level=log_level,
            rate=rate,
            secure=secure,
            signature_check=signature_check,
            slots=slots,
            strict_mode=strict_mode,
        )

        web_default_source_config_source_config.additional_properties = d
        return web_default_source_config_source_config

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
