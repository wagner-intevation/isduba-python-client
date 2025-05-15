# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_workflow_role import ModelsWorkflowRole
from ..models.query_parser_mode import QueryParserMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsStoredQuery")


@_attrs_define
class ModelsStoredQuery:
    """
    Attributes:
        columns (Union[Unset, list[str]]):
        dashboard (Union[Unset, bool]):
        definer (Union[Unset, str]):
        description (Union[Unset, str]):
        global_ (Union[Unset, bool]):
        id (Union[Unset, int]):
        kind (Union[Unset, QueryParserMode]):
        name (Union[Unset, str]):
        num (Union[Unset, int]):
        orders (Union[Unset, list[str]]):
        query (Union[Unset, str]):
        role (Union[Unset, ModelsWorkflowRole]):
    """

    columns: Union[Unset, list[str]] = UNSET
    dashboard: Union[Unset, bool] = UNSET
    definer: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    global_: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    kind: Union[Unset, QueryParserMode] = UNSET
    name: Union[Unset, str] = UNSET
    num: Union[Unset, int] = UNSET
    orders: Union[Unset, list[str]] = UNSET
    query: Union[Unset, str] = UNSET
    role: Union[Unset, ModelsWorkflowRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        dashboard = self.dashboard

        definer = self.definer

        description = self.description

        global_ = self.global_

        id = self.id

        kind: Union[Unset, int] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        num = self.num

        orders: Union[Unset, list[str]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = self.orders

        query = self.query

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if definer is not UNSET:
            field_dict["definer"] = definer
        if description is not UNSET:
            field_dict["description"] = description
        if global_ is not UNSET:
            field_dict["global"] = global_
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if num is not UNSET:
            field_dict["num"] = num
        if orders is not UNSET:
            field_dict["orders"] = orders
        if query is not UNSET:
            field_dict["query"] = query
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        columns = cast(list[str], d.pop("columns", UNSET))

        dashboard = d.pop("dashboard", UNSET)

        definer = d.pop("definer", UNSET)

        description = d.pop("description", UNSET)

        global_ = d.pop("global", UNSET)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, QueryParserMode]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = QueryParserMode(_kind)

        name = d.pop("name", UNSET)

        num = d.pop("num", UNSET)

        orders = cast(list[str], d.pop("orders", UNSET))

        query = d.pop("query", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ModelsWorkflowRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ModelsWorkflowRole(_role)

        models_stored_query = cls(
            columns=columns,
            dashboard=dashboard,
            definer=definer,
            description=description,
            global_=global_,
            id=id,
            kind=kind,
            name=name,
            num=num,
            orders=orders,
            query=query,
            role=role,
        )

        models_stored_query.additional_properties = d
        return models_stored_query

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
