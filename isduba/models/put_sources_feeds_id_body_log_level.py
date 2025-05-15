# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class PutSourcesFeedsIdBodyLogLevel(str, Enum):
    VALUE_0 = "1"
    VALUE_1 = "0"
    VALUE_2 = "1"
    VALUE_3 = "2"
    VALUE_4 = "3"

    def __str__(self) -> str:
        return str(self.value)
