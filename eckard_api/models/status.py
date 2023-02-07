from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact


class Status(SoftDeleteModel):
  status = models.CharField(max_length=50)
  statusLabel = models.CharField(max_length=50, null= True, blank=True)
  stage = models.CharField(max_length=50)
  explanation = models.CharField(max_length=2000, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='status_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='status_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='status_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "status"

