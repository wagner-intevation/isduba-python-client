# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class PutQueriesIdBodyRole(str, Enum):
    ADMIN = "admin"
    AUDITOR = "auditor"
    EDITOR = "editor"
    IMPORTER = "importer"
    REVIEWER = "reviewer"
    SOURCE_MANAGER = "source-manager"

    def __str__(self) -> str:
        return str(self.value)
