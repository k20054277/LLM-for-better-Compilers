import requests

def test_assert():
    response = requests.get('https://api.github.com/users/octocat')
    assert response.status_code == 200
    print(response.json()['name'])

test_assert()