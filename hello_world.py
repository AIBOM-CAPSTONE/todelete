import requests

response = requests.get('https://httpbin.org/ip')

print("Hello, World!")
print('Your IP is {0}'.format(response.json()['origin']))
print("Thanks for testing this out!")