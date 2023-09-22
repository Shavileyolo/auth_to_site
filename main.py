import requests
import credentials as cr

session = requests.Session()

login_url = 'https://www.noob-club.ru/index.php?action=login'

login_data = {
    'username': cr.username,
    'password': cr.password
}

response = session.post(login_url, data=login_data)

print(response)

if response.status_code == 200:
    print('Authorization successful')
else:
    print('Authorization failed')
