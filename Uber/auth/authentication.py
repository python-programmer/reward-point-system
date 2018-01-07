from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from rest_framework_sso import claims
from rest_framework_sso.utils import exceptions


def authenticate_payload(payload):
    user_model = get_user_model()
    user, created = user_model.objects.get_or_create(
        service=payload.get(claims.ISSUER),
        external_id=payload.get(claims.USER_ID),
    )
    if not user.is_active:
        raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
    return user