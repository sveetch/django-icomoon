
from django.urls import reverse


def test_view_from_admin(admin_client):
    """
    Admin can reach authenticated view
    """
    response = admin_client.get(reverse("icomoon:index"))
    assert response.status_code == 200


def test_view_from_user(client):
    """
    Anonymous user is redirected to login page
    """
    response = client.get(reverse("icomoon:index"))
    assert response.status_code == 302
