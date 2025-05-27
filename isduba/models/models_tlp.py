# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class ModelsTLP(str, Enum):
    AMBER = "AMBER"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"

    def __str__(self) -> str:
        return str(self.value)
