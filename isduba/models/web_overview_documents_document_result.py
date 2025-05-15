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
    from ..models.web_overview_documents_document_result_documents_item import (
        WebOverviewDocumentsDocumentResultDocumentsItem,
    )


T = TypeVar("T", bound="WebOverviewDocumentsDocumentResult")


@_attrs_define
class WebOverviewDocumentsDocumentResult:
    """
    Attributes:
        count (Union[Unset, int]):
        documents (Union[Unset, list['WebOverviewDocumentsDocumentResultDocumentsItem']]):
    """

    count: Union[Unset, int] = UNSET
    documents: Union[Unset, list["WebOverviewDocumentsDocumentResultDocumentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_overview_documents_document_result_documents_item import (
            WebOverviewDocumentsDocumentResultDocumentsItem,
        )

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = WebOverviewDocumentsDocumentResultDocumentsItem.from_dict(documents_item_data)

            documents.append(documents_item)

        web_overview_documents_document_result = cls(
            count=count,
            documents=documents,
        )

        web_overview_documents_document_result.additional_properties = d
        return web_overview_documents_document_result

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
