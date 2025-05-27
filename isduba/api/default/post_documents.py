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
from ...models.models_id import ModelsID
from ...models.post_documents_body import PostDocumentsBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostDocumentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ModelsError, ModelsID]]:
    if response.status_code == 201:
        response_201 = ModelsID.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ModelsError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = ModelsError.from_dict(response.json())

        return response_403
    if response.status_code == 409:
        response_409 = ModelsError.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = ModelsError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ModelsError, ModelsID]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    body: PostDocumentsBody,
) -> Response[Union[Any, ModelsError, ModelsID]]:
    """Imports a CSAF document.

     Upload endpoint for CSAF documents.

    Args:
        body (PostDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, ModelsID]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    body: PostDocumentsBody,
) -> Optional[Union[Any, ModelsError, ModelsID]]:
    """Imports a CSAF document.

     Upload endpoint for CSAF documents.

    Args:
        body (PostDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, ModelsID]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    body: PostDocumentsBody,
) -> Response[Union[Any, ModelsError, ModelsID]]:
    """Imports a CSAF document.

     Upload endpoint for CSAF documents.

    Args:
        body (PostDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, ModelsID]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    body: PostDocumentsBody,
) -> Optional[Union[Any, ModelsError, ModelsID]]:
    """Imports a CSAF document.

     Upload endpoint for CSAF documents.

    Args:
        body (PostDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, ModelsID]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
