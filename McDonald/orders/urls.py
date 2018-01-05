from django.conf.urls import url
from .views import OrderList, OrderDetail

urlpatterns = [
    url(r'^$', OrderList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', OrderDetail.as_view())
]