import pytest


@pytest.fixture
def user_data():
    return {'password': 'user_password',
            'password_2': 'user_password',
            'username': 'user_name',
            'first_name': 'user_first_name',
            'last_name': 'user_last_name',
            'email': 'user_email',
            }
