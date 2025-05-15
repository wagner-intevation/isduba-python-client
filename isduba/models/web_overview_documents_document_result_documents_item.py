# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.web_overview_documents_document_result_documents_item_additional_property import (
        WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty,
    )


T = TypeVar("T", bound="WebOverviewDocumentsDocumentResultDocumentsItem")


@_attrs_define
class WebOverviewDocumentsDocumentResultDocumentsItem:
    """ """

    additional_properties: dict[str, "WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty"] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_overview_documents_document_result_documents_item_additional_property import (
            WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty,
        )

        d = dict(src_dict)
        web_overview_documents_document_result_documents_item = cls()

        web_overview_documents_document_result_documents_item.additional_properties = d
        return web_overview_documents_document_result_documents_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
