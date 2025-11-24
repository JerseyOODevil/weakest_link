import requests

url = 'https://api.waifu.im/search'
params = {
    'included_tags': ['maid'],
    'height': '>=2000'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
    # Process the response data as needed
else:
    print('Request failed with status code:', response.status_code)