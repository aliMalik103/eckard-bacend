from django.db import models
from .soft_delete_query_set import SoftDeleteQuerySet


class SoftDeleteManager(models.Manager):
  def get_queryset(self):
      return SoftDeleteQuerySet(self.model, self._db).filter(isDeleted=False)
