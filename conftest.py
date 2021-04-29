import pytest
import requests

@pytest.fixture()
def base_url():
    return"http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture()
def book(base_url):
    book_data = {"title":"world_book", "author":"people"}
    resp = requests.post(f'{base_url}/books', data = book_data)
    book = resp.json()
    yield book
    resp = requests.delete(f'{base_url}/books/{book["id"]}')
    #print(resp.status_code)