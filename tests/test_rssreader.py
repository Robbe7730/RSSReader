import pytest
import os
import tempfile

import pytest

from rssreader import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        return client

def test_sanity():
    assert True
    
def test_root(client):
    rv = client.get('/')
    assert rv != ""
