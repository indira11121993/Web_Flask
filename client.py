import requests

response = requests.post('http://127.0.0.1:5000/advt/',
                         json={
                             'title': 'some Advertisement',
                             'author': 'user1',
                             'description': 'some description'
                               })
print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/advt/1')
print(response.status_code)
print(response.json())

response = requests.patch('http://127.0.0.1:5000/advt/1', json={
                                                            'title': 'fix title',
                                                            'description': 'new description',
                                                            'author': 'user1'
                                                            })

response = requests.get('http://127.0.0.1:5000/advt/1')
print(response.status_code)
print(response.json())
#
response = requests.delete('http://127.0.0.1:5000/advt/1')
print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/advt/1')
print(response.status_code)
print(response.json())