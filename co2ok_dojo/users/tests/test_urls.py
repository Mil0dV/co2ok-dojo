import pytest
from django.conf import settings
from django.urls import reverse, resolve

class TestUrls:

    def test_invitation_page_url(self):
#         assert reverse("users:list") == "/users/"
#         assert resolve("/users/").view_name == "users:list"
        path = reverse('invitation_page', kwargs={'user_id':1})
        assert resolve(path).view_name == 'invitation_page'
