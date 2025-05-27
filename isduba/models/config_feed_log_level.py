# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import IntEnum


class ConfigFeedLogLevel(IntEnum):
    DEFAULT_SOURCES_FEED_LOG_LEVEL = 1
    DEBUG_FEED_LOG_LEVEL = 0
    INFO_FEED_LOG_LEVEL = 1
    WARN_FEED_LOG_LEVEL = 2
    ERROR_FEED_LOG_LEVEL = 3

    def __str__(self) -> str:
        return str(self.value)
