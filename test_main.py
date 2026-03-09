"""
Unit tests for the Flask app.
"""

import json
from main import app


@pytest.fixture
def client():
    """Create a test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200


def test_greet_api(client):
    """Test the greet API endpoint."""
    response = client.post('/api/greet', 
                          json={'name': 'Flask'},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Hello, Flask!'


def test_sum_api(client):
    """Test the sum API endpoint."""
    response = client.post('/api/sum',
                          json={'numbers': [1, 2, 3, 4, 5]},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 15
    assert data['numbers'] == [1, 2, 3, 4, 5]
