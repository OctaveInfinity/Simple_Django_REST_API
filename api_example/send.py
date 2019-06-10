import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGiOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYwMTU2MzE1LCJqdGkiOiIyNjBlYWQyODc0MTE0ZjZmOWNjMzU3MGZiNGFiYTg3MyIsInVzZXJfaWQiOjJ9.OCpObK98uSudQ6VWy3E9rDvWP2UOF2oCFk_2daXr22M'

r = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)

print(r.text)