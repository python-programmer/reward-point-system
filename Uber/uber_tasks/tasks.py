from __future__ import absolute_import, unicode_literals
from .celery import app
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Uber.settings")
django.setup()

from orders.models import Order

@app.task(name='change_attributes', queue='uber')
def change_attributes(**kwargs):
    for order in Order.objects.all():
        order.item.update(kwargs)
        order.save()
