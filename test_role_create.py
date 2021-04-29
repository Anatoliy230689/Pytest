import requests


def test_craete_role(book, base_url):
    role_data = {
        "name": "Winston Smith",
        "type": "Free man",
        "level": 37,
        "book": book['id']
    }
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 201
    resp_body = resp.json()
    print(f'\n {role_data}')
    print(resp_body)
    assert  'id' in resp_body
    for key in role_data:
        assert role_data[key] == resp_body[key]

    resp_get = requests.get(f'{base_url}/roles/{resp_body["id"]}')
    assert resp_get.status_code == 200
    resp_body = resp_get.json()