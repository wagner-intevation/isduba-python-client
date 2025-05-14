<!--
SPDX-FileCopyrightText: 2025 Intevation GmbH

SPDX-License-Identifier: Apache-2.0
-->

# ISDuBA Python Client
A client library for accessing ISDuBA API

## Usage
First, create a client instance:

```python
from isduba import Client

client = Client(base_url="https://isduba.example.com")
```

The, login with your credentials:
```python
client.login(username='ada', password='bob')
```
