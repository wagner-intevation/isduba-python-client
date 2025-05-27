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
    from ..models.web_source import WebSource


T = TypeVar("T", bound="WebViewSourcesSourcesResult")


@_attrs_define
class WebViewSourcesSourcesResult:
    """
    Attributes:
        sources (Union[Unset, list['WebSource']]):
    """

    sources: Union[Unset, list["WebSource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_source import WebSource

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = WebSource.from_dict(sources_item_data)

            sources.append(sources_item)

        web_view_sources_sources_result = cls(
            sources=sources,
        )

        web_view_sources_sources_result.additional_properties = d
        return web_view_sources_sources_result

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
