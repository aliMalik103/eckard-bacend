from django.db import models
from .deleted_query_set import DeletedQuerySet

class DeletedManager(models.Manager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, self._db).filter(isDeleted=True)
