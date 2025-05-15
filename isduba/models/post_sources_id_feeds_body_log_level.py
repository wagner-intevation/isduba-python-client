# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class PostSourcesIdFeedsBodyLogLevel(str, Enum):
    DEBUG = "debug"
    ERROR = "error"
    INFO = "info"
    VALUE_4 = ""
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
