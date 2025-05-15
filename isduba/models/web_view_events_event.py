# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_event import ModelsEvent
from ..models.models_workflow import ModelsWorkflow
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebViewEventsEvent")


@_attrs_define
class WebViewEventsEvent:
    """
    Attributes:
        actor (Union[Unset, str]):
        comment_id (Union[Unset, int]):
        document_id (Union[Unset, int]):
        event_type (Union[Unset, ModelsEvent]):
        state (Union[Unset, ModelsWorkflow]):
        time (Union[Unset, str]):
    """

    actor: Union[Unset, str] = UNSET
    comment_id: Union[Unset, int] = UNSET
    document_id: Union[Unset, int] = UNSET
    event_type: Union[Unset, ModelsEvent] = UNSET
    state: Union[Unset, ModelsWorkflow] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor = self.actor

        comment_id = self.comment_id

        document_id = self.document_id

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actor is not UNSET:
            field_dict["actor"] = actor
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if state is not UNSET:
            field_dict["state"] = state
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actor = d.pop("actor", UNSET)

        comment_id = d.pop("comment_id", UNSET)

        document_id = d.pop("document_id", UNSET)

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, ModelsEvent]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = ModelsEvent(_event_type)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ModelsWorkflow]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ModelsWorkflow(_state)

        time = d.pop("time", UNSET)

        web_view_events_event = cls(
            actor=actor,
            comment_id=comment_id,
            document_id=document_id,
            event_type=event_type,
            state=state,
            time=time,
        )

        web_view_events_event.additional_properties = d
        return web_view_events_event

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
