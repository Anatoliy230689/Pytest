import pytest
import requests

@pytest.fixture()
def base_url():
    return"http://pulse-rest-testing.herokuapp.com/"

