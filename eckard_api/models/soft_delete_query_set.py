from django.db import models
from django.conf import settings
from django.utils import timezone

def get_settings():
    default_settings = dict(
        cascade=True,
    )
    return getattr(settings, 'DJANGO_SOFTDELETE_SETTINGS', default_settings)


class SoftDeleteQuerySet(models.query.QuerySet):
  def delete(self, cascade=None):
      cascade = get_settings()['cascade']
      if cascade:  # delete one by one if cascade
          for obj in self.all():
              obj.delete(cascade=cascade)
      return self.update(isDeleted=True, deletedAt=timezone.now())

  def hard_delete(self):
      return super().delete()
