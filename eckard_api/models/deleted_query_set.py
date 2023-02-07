from django.db import models


class DeletedQuerySet(models.query.QuerySet):
  def restore(self, *args, **kwargs):
      qs = self.filter(*args, **kwargs)
      qs.update(isDeleted=False, deletedAt=None)