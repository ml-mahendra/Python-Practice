
# For errors check 'https://cutt.ly/api-documentation/regular-api'

# To run this program, requests package is needed. Use pip install requests, if you dont have already.

import requests


def short_link (full_link, link_name):
    API_KEY = "a8a4c877b7919a7d39485970be57bfe0c996c"

    BASE_URL = "https://cutt.ly/api/api.php"
    
    
    payload = {'key':API_KEY, 'short':full_link, 'name': link_name}
    request = requests.get(BASE_URL, params = payload)
    data = request.json()
    
    print('')
    
    try:
        title = data['url']['title']
        s_link = data['url']['shortLink']
        
        print('Title:', title)
        print('Link:', s_link)
        
    except:
        status = data['url']['status']
        print('Error Status:', status)
        
        

usr_link_inp = input("Enter the actual Link: ")
usr_link_name = input('Enter your link name:')
short_link(usr_link_inp, usr_link_name)


