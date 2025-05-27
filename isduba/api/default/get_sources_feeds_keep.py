# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.web_keep_feed_time_keep_feed_time_config import WebKeepFeedTimeKeepFeedTimeConfig
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sources/feeds/keep",
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]:
    if response.status_code == 200:
        response_200 = WebKeepFeedTimeKeepFeedTimeConfig.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]:
    """Returns how long feed logs are kept.

     Returns the time it takes until old feed entries are deleted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]:
    """Returns how long feed logs are kept.

     Returns the time it takes until old feed entries are deleted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]:
    """Returns how long feed logs are kept.

     Returns the time it takes until old feed entries are deleted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]]:
    """Returns how long feed logs are kept.

     Returns the time it takes until old feed entries are deleted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebKeepFeedTimeKeepFeedTimeConfig]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
