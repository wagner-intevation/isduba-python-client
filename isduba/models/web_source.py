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
    from ..models.sources_stats import SourcesStats
    from ..models.web_source_age import WebSourceAge


T = TypeVar("T", bound="WebSource")


@_attrs_define
class WebSource:
    """
    Attributes:
        name (str):
        url (str):
        active (Union[Unset, bool]):
        age (Union[Unset, WebSourceAge]):
        attention (Union[Unset, bool]):
        client_cert_passphrase (Union[Unset, str]):
        client_cert_private (Union[Unset, str]):
        client_cert_public (Union[Unset, str]):
        headers (Union[Unset, list[str]]):
        id (Union[Unset, int]):
        ignore_patterns (Union[Unset, list[str]]):
        rate (Union[Unset, float]):
        secure (Union[Unset, bool]):
        signature_check (Union[Unset, bool]):
        slots (Union[Unset, int]):
        stats (Union[Unset, SourcesStats]):
        status (Union[Unset, list[str]]):
        strict_mode (Union[Unset, bool]):
    """

    name: str
    url: str
    active: Union[Unset, bool] = UNSET
    age: Union[Unset, "WebSourceAge"] = UNSET
    attention: Union[Unset, bool] = UNSET
    client_cert_passphrase: Union[Unset, str] = UNSET
    client_cert_private: Union[Unset, str] = UNSET
    client_cert_public: Union[Unset, str] = UNSET
    headers: Union[Unset, list[str]] = UNSET
    id: Union[Unset, int] = UNSET
    ignore_patterns: Union[Unset, list[str]] = UNSET
    rate: Union[Unset, float] = UNSET
    secure: Union[Unset, bool] = UNSET
    signature_check: Union[Unset, bool] = UNSET
    slots: Union[Unset, int] = UNSET
    stats: Union[Unset, "SourcesStats"] = UNSET
    status: Union[Unset, list[str]] = UNSET
    strict_mode: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        active = self.active

        age: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.age, Unset):
            age = self.age.to_dict()

        attention = self.attention

        client_cert_passphrase = self.client_cert_passphrase

        client_cert_private = self.client_cert_private

        client_cert_public = self.client_cert_public

        headers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers

        id = self.id

        ignore_patterns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ignore_patterns, Unset):
            ignore_patterns = self.ignore_patterns

        rate = self.rate

        secure = self.secure

        signature_check = self.signature_check

        slots = self.slots

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        status: Union[Unset, list[str]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        strict_mode = self.strict_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if age is not UNSET:
            field_dict["age"] = age
        if attention is not UNSET:
            field_dict["attention"] = attention
        if client_cert_passphrase is not UNSET:
            field_dict["client_cert_passphrase"] = client_cert_passphrase
        if client_cert_private is not UNSET:
            field_dict["client_cert_private"] = client_cert_private
        if client_cert_public is not UNSET:
            field_dict["client_cert_public"] = client_cert_public
        if headers is not UNSET:
            field_dict["headers"] = headers
        if id is not UNSET:
            field_dict["id"] = id
        if ignore_patterns is not UNSET:
            field_dict["ignore_patterns"] = ignore_patterns
        if rate is not UNSET:
            field_dict["rate"] = rate
        if secure is not UNSET:
            field_dict["secure"] = secure
        if signature_check is not UNSET:
            field_dict["signature_check"] = signature_check
        if slots is not UNSET:
            field_dict["slots"] = slots
        if stats is not UNSET:
            field_dict["stats"] = stats
        if status is not UNSET:
            field_dict["status"] = status
        if strict_mode is not UNSET:
            field_dict["strict_mode"] = strict_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources_stats import SourcesStats
        from ..models.web_source_age import WebSourceAge

        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        active = d.pop("active", UNSET)

        _age = d.pop("age", UNSET)
        age: Union[Unset, WebSourceAge]
        if isinstance(_age, Unset):
            age = UNSET
        else:
            age = WebSourceAge.from_dict(_age)

        attention = d.pop("attention", UNSET)

        client_cert_passphrase = d.pop("client_cert_passphrase", UNSET)

        client_cert_private = d.pop("client_cert_private", UNSET)

        client_cert_public = d.pop("client_cert_public", UNSET)

        headers = cast(list[str], d.pop("headers", UNSET))

        id = d.pop("id", UNSET)

        ignore_patterns = cast(list[str], d.pop("ignore_patterns", UNSET))

        rate = d.pop("rate", UNSET)

        secure = d.pop("secure", UNSET)

        signature_check = d.pop("signature_check", UNSET)

        slots = d.pop("slots", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, SourcesStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = SourcesStats.from_dict(_stats)

        status = cast(list[str], d.pop("status", UNSET))

        strict_mode = d.pop("strict_mode", UNSET)

        web_source = cls(
            name=name,
            url=url,
            active=active,
            age=age,
            attention=attention,
            client_cert_passphrase=client_cert_passphrase,
            client_cert_private=client_cert_private,
            client_cert_public=client_cert_public,
            headers=headers,
            id=id,
            ignore_patterns=ignore_patterns,
            rate=rate,
            secure=secure,
            signature_check=signature_check,
            slots=slots,
            stats=stats,
            status=status,
            strict_mode=strict_mode,
        )

        web_source.additional_properties = d
        return web_source

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
