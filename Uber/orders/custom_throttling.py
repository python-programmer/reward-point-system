from rest_framework import throttling
from rest_framework import permissions
from django.core.cache import cache
from django.conf import settings


class PerUserRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        if settings.UNSAFE_METHODS_THROTTLE_RATE is None:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        num_of_request = cache.get(request.session.get('username'))
        timeout = cache.ttl(request.session.get('username'))
        if num_of_request is None:
            cache.set(request.session.get('username'), 1, timeout=settings.UNSAFE_METHODS_THROTTLE_TIME)
            return True

        if num_of_request >= settings.UNSAFE_METHODS_THROTTLE_RATE:
            return False

        cache.set(request.session.get('username'), num_of_request + 1, timeout=timeout)
        return True
