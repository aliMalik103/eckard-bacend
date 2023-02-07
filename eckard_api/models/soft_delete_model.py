from django.db import models
from .soft_delete_manager import SoftDeleteManager
from .deleted_manager import DeletedManager
from .global_manager import GlobalManager
from django.utils import timezone
from django.conf import settings

def get_settings():
  default_settings = dict(
      cascade=True,
  )
  return getattr(settings, 'DJANGO_SOFTDELETE_SETTINGS', default_settings)


class SoftDeleteModel(models.Model):
  isDeleted = models.BooleanField(default=False, blank=True, null=True)
  deletedAt = models.DateTimeField(blank=True, null=True)

  objects = SoftDeleteManager()
  deleted_objects = DeletedManager()
  global_objects = GlobalManager()

  class Meta:
      abstract = True

  def delete(self, cascade=None, *args, **kwargs):
    cascade = get_settings()['cascade']
    self.isDeleted = True
    self.deletedAt = timezone.now()
    self.save()
    self.after_delete()
    if cascade:
        self.delete_related_objects()

  def restore(self, cascade=None):
    cascade = get_settings()['cascade']
    self.isDeleted = False
    self.deletedAt = None
    self.save()
    self.after_restore()
    if cascade:
        self.restore_related_objects()

  def hard_delete(self, *args, **kwargs):
    super().delete(*args, **kwargs)

  def get_related_objects(self):
    return []

  def delete_related_objects(self):
    for obj in self.get_related_objects():
        obj.delete()

  def restore_related_objects(self):
    for obj in self.get_related_objects():
        obj.restore()

  def after_delete(self):
    pass

  def after_restore(self):
    pass