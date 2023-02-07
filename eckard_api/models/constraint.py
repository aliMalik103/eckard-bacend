from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact


class Constraint(SoftDeleteModel):
  constraint = models.CharField(max_length=100)
  constraintLabel = models.CharField(max_length=100, null= True, blank=True)
  constraintType = models.CharField(max_length=100, null= True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='constraint_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='constraint_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='constraint_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "constraint"

