# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class PostQueriesBodyKind(str, Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"

    def __str__(self) -> str:
        return str(self.value)
