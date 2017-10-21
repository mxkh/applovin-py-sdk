[![Build Status](https://travis-ci.org/mxkh/applovin-py-sdk.svg?branch=master)](https://travis-ci.org/mxkh/applovin-py-sdk)

Simple Python SDK that helps make requests to Applovin mobile ad network

```python
from request import Request

request = Request(
    'api key',
    '2017-09-20',
    '2017-09-20'
)

request.columns = ['day', 'impressions', 'revenue', 'ctr']

response = request.make()

print(response.json())
```