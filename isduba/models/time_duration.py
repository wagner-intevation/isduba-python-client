# generated with https://github.com/openapi-generators/openapi-python-client

# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import IntEnum


class TimeDuration(IntEnum):
    MIN_DURATION = -9223372036854776000
    MAX_DURATION = 9223372036854776000
    NANOSECOND = 1
    MICROSECOND = 1000
    MILLISECOND = 1000000
    SECOND = 1000000000
    MINUTE = 60000000000
    HOUR = 3600000000000

    def __str__(self) -> str:
        return str(self.value)
