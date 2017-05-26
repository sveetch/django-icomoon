import pytest

from django.core.urlresolvers import reverse


def test_ping_index(admin_client):
    """Just pinging bazar index page"""
    response = admin_client.get(reverse('icomoon:index'))
    assert response.status_code == 200
