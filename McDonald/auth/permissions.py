from rest_framework import permissions
from rest_framework.status import HTTP_200_OK
from rest_framework.request import HttpRequest
from django.conf import settings


class IsSSOAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        :type request HttpRequest
        """
        import json
        import requests
        if settings.AUTHORIZATION_HEADER in request.META:
            token = request.META.get(settings.AUTHORIZATION_HEADER, ' ').split(' ')[1]
            result = requests.post(settings.SSO_VERIFY_TOKEN_SERVER, data={'token': token})
            if result.status_code == HTTP_200_OK:
                request.session['username'] = result.json()['user']['username']
                return True
        return False


