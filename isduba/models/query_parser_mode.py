# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import IntEnum


class QueryParserMode(IntEnum):
    DOCUMENT_MODE = 0
    ADVISORY_MODE = 1
    EVENT_MODE = 2

    def __str__(self) -> str:
        return str(self.value)
