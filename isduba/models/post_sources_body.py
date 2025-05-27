# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSourcesBody")


@_attrs_define
class PostSourcesBody:
    """
    Attributes:
        name (str):
        url (str):
        active (Union[Unset, bool]):
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
        status (Union[Unset, list[str]]):
        strict_mode (Union[Unset, bool]):
    """

    name: str
    url: str
    active: Union[Unset, bool] = UNSET
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
    status: Union[Unset, list[str]] = UNSET
    strict_mode: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        active = self.active

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
        if status is not UNSET:
            field_dict["status"] = status
        if strict_mode is not UNSET:
            field_dict["strict_mode"] = strict_mode

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        url = (None, str(self.url).encode(), "text/plain")

        active = self.active if isinstance(self.active, Unset) else (None, str(self.active).encode(), "text/plain")

        attention = (
            self.attention if isinstance(self.attention, Unset) else (None, str(self.attention).encode(), "text/plain")
        )

        client_cert_passphrase = (
            self.client_cert_passphrase
            if isinstance(self.client_cert_passphrase, Unset)
            else (None, str(self.client_cert_passphrase).encode(), "text/plain")
        )

        client_cert_private = (
            self.client_cert_private
            if isinstance(self.client_cert_private, Unset)
            else (None, str(self.client_cert_private).encode(), "text/plain")
        )

        client_cert_public = (
            self.client_cert_public
            if isinstance(self.client_cert_public, Unset)
            else (None, str(self.client_cert_public).encode(), "text/plain")
        )

        headers: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.headers, Unset):
            _temp_headers = self.headers
            headers = (None, json.dumps(_temp_headers).encode(), "application/json")

        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        ignore_patterns: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.ignore_patterns, Unset):
            _temp_ignore_patterns = self.ignore_patterns
            ignore_patterns = (None, json.dumps(_temp_ignore_patterns).encode(), "application/json")

        rate = self.rate if isinstance(self.rate, Unset) else (None, str(self.rate).encode(), "text/plain")

        secure = self.secure if isinstance(self.secure, Unset) else (None, str(self.secure).encode(), "text/plain")

        signature_check = (
            self.signature_check
            if isinstance(self.signature_check, Unset)
            else (None, str(self.signature_check).encode(), "text/plain")
        )

        slots = self.slots if isinstance(self.slots, Unset) else (None, str(self.slots).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            _temp_status = self.status
            status = (None, json.dumps(_temp_status).encode(), "application/json")

        strict_mode = (
            self.strict_mode
            if isinstance(self.strict_mode, Unset)
            else (None, str(self.strict_mode).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
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
        if status is not UNSET:
            field_dict["status"] = status
        if strict_mode is not UNSET:
            field_dict["strict_mode"] = strict_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        active = d.pop("active", UNSET)

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

        status = cast(list[str], d.pop("status", UNSET))

        strict_mode = d.pop("strict_mode", UNSET)

        post_sources_body = cls(
            name=name,
            url=url,
            active=active,
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
            status=status,
            strict_mode=strict_mode,
        )

        post_sources_body.additional_properties = d
        return post_sources_body

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
