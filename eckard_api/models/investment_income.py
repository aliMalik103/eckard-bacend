from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact
from .investment import Investment
from .cash_flow import CashFlow

class InvestmentIncome(SoftDeleteModel):
  investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
  income = models.DecimalField(max_digits=9, decimal_places=2)
  cash_flow = models.ForeignKey(CashFlow, on_delete=models.CASCADE)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='investment_income_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='investment_income_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='investment_income_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "investment_income"
        
