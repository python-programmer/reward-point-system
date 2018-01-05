import collections
from django.db import models
from jsonfield import JSONField


class Order(models.Model):
    user_name = models.CharField(max_length=200, null=True)
    item = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
    checkout_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0!s} order: {1!s}'.format(self.user_name, self.item)
