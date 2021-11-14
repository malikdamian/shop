import pytest
from django.contrib.auth.models import User
from django import urls


@pytest.mark.parametrize('param', [
    'accounts:login',
    'accounts:register',
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_signup(client, user_data):
    assert User.objects.count() == 0
    signup_url = urls.reverse('accounts:register')
    resp = client.post(signup_url, user_data)
    assert resp.status_code == 200
