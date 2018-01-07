from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from admin_tasks.celery import app


class ClientList(APIView):

    def get(self, request, format=None):
        return Response(settings.CLIENTS)

    def post(self, request, format=None):
        client = request.data.get('client', None)
        if client is None:
            return Response({'detail': 'client must be selected'}, status=HTTP_400_BAD_REQUEST)

        if client not in settings.CLIENTS:
            return Response({'detail': 'client not found'}, status=HTTP_404_NOT_FOUND)

        attributes = dict([item for item in request.data.items() if item[0] != 'client'])

        if not len(attributes):
            return Response({'detail': 'at least one attr required'}, status=HTTP_400_BAD_REQUEST)

        app.send_task(settings.CHANGE_ATTRIBUTES, kwargs=attributes, queue=client)

        return Response(request.data, status=HTTP_201_CREATED)
