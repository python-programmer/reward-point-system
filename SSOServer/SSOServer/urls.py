from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from auth.views import SignUp

urlpatterns = [
    url(r'^sign-up/$', SignUp.as_view()),
    url(r'^clients/', include('client.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
