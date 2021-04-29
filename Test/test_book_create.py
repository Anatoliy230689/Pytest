import requests

#book create and read
def test_book_creare(base_url):
    book_data = {
        "title": "TITLE",
        "author": "AUTHOR"
    }
    res = requests.post(f'{base_url}/books', data=book_data)
    book = res.json()
    assert res.status_code == 201
    assert 'id' in book
    for key in book_data:
        assert book_data[key] == book[key]

    res_get = requests.get(f'{base_url}/books/{book["id"]}')
    assert res_get.status_code == 200
    new_book = res_get.json()
    new_book.pop('id')
    assert  new_book == book_data







