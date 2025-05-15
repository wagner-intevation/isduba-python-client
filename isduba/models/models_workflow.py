# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class ModelsWorkflow(str, Enum):
    ARCHIVED = "archived"
    ASSESSING = "assessing"
    DELETE = "delete"
    NEW = "new"
    READ = "read"
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
