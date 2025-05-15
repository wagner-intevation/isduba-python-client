# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.models_error import ModelsError
from ...models.web_view_events_event import WebViewEventsEvent
from ...types import Response


def _get_kwargs(
    publisher: str,
    trackingid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/events/{publisher}/{trackingid}",
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ModelsError, list["WebViewEventsEvent"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebViewEventsEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ModelsError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = ModelsError.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ModelsError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ModelsError, list["WebViewEventsEvent"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher: str,
    trackingid: str,
    *,
    client: Client,
) -> Response[Union[Any, ModelsError, list["WebViewEventsEvent"]]]:
    """Returns all events.

     Returns all events from the specified advisory.

    Args:
        publisher (str):
        trackingid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, list['WebViewEventsEvent']]]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        trackingid=trackingid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher: str,
    trackingid: str,
    *,
    client: Client,
) -> Optional[Union[Any, ModelsError, list["WebViewEventsEvent"]]]:
    """Returns all events.

     Returns all events from the specified advisory.

    Args:
        publisher (str):
        trackingid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, list['WebViewEventsEvent']]
    """

    return sync_detailed(
        publisher=publisher,
        trackingid=trackingid,
        client=client,
    ).parsed


async def asyncio_detailed(
    publisher: str,
    trackingid: str,
    *,
    client: Client,
) -> Response[Union[Any, ModelsError, list["WebViewEventsEvent"]]]:
    """Returns all events.

     Returns all events from the specified advisory.

    Args:
        publisher (str):
        trackingid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, list['WebViewEventsEvent']]]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        trackingid=trackingid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher: str,
    trackingid: str,
    *,
    client: Client,
) -> Optional[Union[Any, ModelsError, list["WebViewEventsEvent"]]]:
    """Returns all events.

     Returns all events from the specified advisory.

    Args:
        publisher (str):
        trackingid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, list['WebViewEventsEvent']]
    """

    return (
        await asyncio_detailed(
            publisher=publisher,
            trackingid=trackingid,
            client=client,
        )
    ).parsed
