import json, os

if not os.path.exists('users.json'):
    with open("users.json", "w") as file:
        json.dump({
    "users": [
        {"name": "Sri", "age": 20, "email": "sri@lol.com"},
        {"name": "Rii", "age": 40, "email": "rii@lol.com"},
        {"name": "Jai", "age": 30, "email": "jai@lol.com"}
    ]
}, file, indent=4)

json_file_path = 'users.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)
if 'users' in data:
    for user in data['users']:
        print(f"Name: {user['name']}")
else:
    print("No 'users' key found in the JSON data.")
