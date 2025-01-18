import requests

payload = {'name':'morpheus','job':'leader'}
r = requests.post('https://reqres.in/api/users',data=payload)
print(r.text)