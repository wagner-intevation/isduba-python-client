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
from ...models.models_success import ModelsSuccess
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    stats: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["stats"] = stats

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sources/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ModelsError, ModelsSuccess]]:
    if response.status_code == 200:
        response_200 = ModelsSuccess.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ModelsError, ModelsSuccess]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, ModelsError, ModelsSuccess]]:
    """Returns source information.

     Returns the source configuration and metadata.

    Args:
        id (int):
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, ModelsSuccess]]
    """

    kwargs = _get_kwargs(
        id=id,
        stats=stats,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, ModelsError, ModelsSuccess]]:
    """Returns source information.

     Returns the source configuration and metadata.

    Args:
        id (int):
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, ModelsSuccess]
    """

    return sync_detailed(
        id=id,
        client=client,
        stats=stats,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, ModelsError, ModelsSuccess]]:
    """Returns source information.

     Returns the source configuration and metadata.

    Args:
        id (int):
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, ModelsSuccess]]
    """

    kwargs = _get_kwargs(
        id=id,
        stats=stats,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    stats: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, ModelsError, ModelsSuccess]]:
    """Returns source information.

     Returns the source configuration and metadata.

    Args:
        id (int):
        stats (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, ModelsSuccess]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            stats=stats,
        )
    ).parsed
