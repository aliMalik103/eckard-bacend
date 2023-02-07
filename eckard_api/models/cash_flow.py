from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact
from .project import Project
from .account import Account

class CashFlow(SoftDeleteModel):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  paidDate = models.DateField()
  income = models.DecimalField(max_digits=50, decimal_places=10)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='cash_flow_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='cash_flow_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='cash_flow_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "cash_flow"
