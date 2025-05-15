# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_stats_cve_source_id_response_200 import GetStatsCveSourceIdResponse200
from ...models.models_error import ModelsError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    step: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["step"] = step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/stats/cve/source/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]:
    if response.status_code == 200:
        response_200 = GetStatsCveSourceIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ModelsError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = ModelsError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]:
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
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    step: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]:
    """Returns cve statistics.

     Returns cve statistics for the specified source.

    Args:
        id (int):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        step (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        step=step,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Client,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    step: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]:
    """Returns cve statistics.

     Returns cve statistics for the specified source.

    Args:
        id (int):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        step (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStatsCveSourceIdResponse200, ModelsError]
    """

    return sync_detailed(
        id=id,
        client=client,
        from_=from_,
        to=to,
        step=step,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    step: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]:
    """Returns cve statistics.

     Returns cve statistics for the specified source.

    Args:
        id (int):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        step (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        step=step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    step: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetStatsCveSourceIdResponse200, ModelsError]]:
    """Returns cve statistics.

     Returns cve statistics for the specified source.

    Args:
        id (int):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        step (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStatsCveSourceIdResponse200, ModelsError]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_=from_,
            to=to,
            step=step,
        )
    ).parsed
