import requests


API_URL = "http://127.0.0.1:5000/api/v2/"


# All users:
print(requests.get(API_URL + "users").json())

# Correct create user:
print(requests.post(API_URL + "users", json={
    "email": "1@mail.ru",
    "password": "321",
    "name": "name2",
    "surname": "surname2"
}).json())

# Invalid create user (not email):
print(requests.post(API_URL + "users", json={
    "password": "321",
    "name": "name3",
    "surname": "surname3"
}).json())

# All users:
print(requests.get(API_URL + "users").json())

# One user with correct id:
print(requests.get(API_URL + "users/1").json())

# One user with int invalid id:
print(requests.get(API_URL + "users/1000").json())

# One user with string id:
print(requests.get(API_URL + "users/string").json())

# Delete user with correct id:
print(requests.delete(API_URL + "users/2").json())

# Delete user with invalid id:
print(requests.delete(API_URL + "users/2020").json())

# All users:
print(requests.get(API_URL + "users").json())
