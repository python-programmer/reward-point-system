from django.conf.urls import url
from .views import ClientList

urlpatterns = [
    url(r'^$', ClientList.as_view()),
]
