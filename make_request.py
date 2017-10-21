from request import Request

request = Request(
    'api key',
    '2017-09-20',
    '2017-09-20'
)

request.columns = ['day', 'impressions', 'revenue', 'ctr']

response = request.make()

print(response.json())
