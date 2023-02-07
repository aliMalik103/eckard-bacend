from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact

class KeyValue(SoftDeleteModel):
  key = models.CharField(max_length=200, null=True, blank=True)
  value1 = models.CharField(max_length=2000, null=True, blank=True)
  value2 = models.CharField(max_length=200, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='keyvalue_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='keyvalue_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='keyvalue_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "key_value"

