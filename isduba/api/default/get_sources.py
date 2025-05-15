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
from ...models.web_view_sources_sources_result import WebViewSourcesSourcesResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    stats: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["stats"] = stats

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ModelsError, WebViewSourcesSourcesResult]]:
    if response.status_code == 200:
        response_200 = WebViewSourcesSourcesResult.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ModelsError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ModelsError, WebViewSourcesSourcesResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, ModelsError, WebViewSourcesSourcesResult]]:
    """Returns all sources.

     Returns the source configuration and metadata of all sources.

    Args:
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, WebViewSourcesSourcesResult]]
    """

    kwargs = _get_kwargs(
        stats=stats,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, ModelsError, WebViewSourcesSourcesResult]]:
    """Returns all sources.

     Returns the source configuration and metadata of all sources.

    Args:
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, WebViewSourcesSourcesResult]
    """

    return sync_detailed(
        client=client,
        stats=stats,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, ModelsError, WebViewSourcesSourcesResult]]:
    """Returns all sources.

     Returns the source configuration and metadata of all sources.

    Args:
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, WebViewSourcesSourcesResult]]
    """

    kwargs = _get_kwargs(
        stats=stats,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, ModelsError, WebViewSourcesSourcesResult]]:
    """Returns all sources.

     Returns the source configuration and metadata of all sources.

    Args:
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, WebViewSourcesSourcesResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            stats=stats,
        )
    ).parsed
