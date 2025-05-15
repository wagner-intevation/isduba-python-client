# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

from enum import Enum


class ModelsEvent(str, Enum):
    ADD_COMMENT = "add_comment"
    ADD_SSCV = "add_sscv"
    CHANGE_COMMENT = "change_comment"
    CHANGE_SSCV = "change_sscv"
    DELETE_COMMENT = "delete_comment"
    DELETE_DOCUMENT = "delete_document"
    DELETE_SSCV = "delete_sscv"
    IMPORT_DOCUMENT = "import_document"
    STATE_CHANGE = "state_change"

    def __str__(self) -> str:
        return str(self.value)
