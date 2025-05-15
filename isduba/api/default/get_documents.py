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
from ...models.web_overview_documents_document_result import WebOverviewDocumentsDocumentResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    advisories: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    orders: Union[Unset, str] = UNSET,
    count: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["advisories"] = advisories

    params["query"] = query

    params["columns"] = columns

    params["orders"] = orders

    params["count"] = count

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]:
    if response.status_code == 200:
        response_200 = WebOverviewDocumentsDocumentResult.from_dict(response.json())

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
) -> Response[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    advisories: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    orders: Union[Unset, str] = UNSET,
    count: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]:
    """Returns documents.

     Returns all documents that match the specified query.

    Args:
        advisories (Union[Unset, bool]):
        query (Union[Unset, str]):
        columns (Union[Unset, str]):
        orders (Union[Unset, str]):
        count (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]
    """

    kwargs = _get_kwargs(
        advisories=advisories,
        query=query,
        columns=columns,
        orders=orders,
        count=count,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    advisories: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    orders: Union[Unset, str] = UNSET,
    count: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]:
    """Returns documents.

     Returns all documents that match the specified query.

    Args:
        advisories (Union[Unset, bool]):
        query (Union[Unset, str]):
        columns (Union[Unset, str]):
        orders (Union[Unset, str]):
        count (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]
    """

    return sync_detailed(
        client=client,
        advisories=advisories,
        query=query,
        columns=columns,
        orders=orders,
        count=count,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    advisories: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    orders: Union[Unset, str] = UNSET,
    count: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]:
    """Returns documents.

     Returns all documents that match the specified query.

    Args:
        advisories (Union[Unset, bool]):
        query (Union[Unset, str]):
        columns (Union[Unset, str]):
        orders (Union[Unset, str]):
        count (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]
    """

    kwargs = _get_kwargs(
        advisories=advisories,
        query=query,
        columns=columns,
        orders=orders,
        count=count,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    advisories: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    orders: Union[Unset, str] = UNSET,
    count: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]]:
    """Returns documents.

     Returns all documents that match the specified query.

    Args:
        advisories (Union[Unset, bool]):
        query (Union[Unset, str]):
        columns (Union[Unset, str]):
        orders (Union[Unset, str]):
        count (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ModelsError, WebOverviewDocumentsDocumentResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            advisories=advisories,
            query=query,
            columns=columns,
            orders=orders,
            count=count,
            limit=limit,
            offset=offset,
        )
    ).parsed
