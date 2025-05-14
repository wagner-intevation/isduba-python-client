# ISDuBA Python Client
A client library for accessing ISDuBA API

## Usage
First, create a client:

```python
from isduba import Client

client = Client(base_url="https://isduba.example.com")
```

The, login with your credentials:
```python
client.login(username='ada', password='bob')
```
