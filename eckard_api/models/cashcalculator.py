from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact


class CashCalculator(SoftDeleteModel):
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null= True, blank=True)
  noOfMonths = models.IntegerField(null= True, blank=True)
  decline =  models.DecimalField(max_digits=12, decimal_places=5, null= True, blank=True)
  oilPrice = models.DecimalField(max_digits=12, decimal_places=5, null= True, blank=True)
  gasPrice =  models.DecimalField(max_digits=12, decimal_places=5, null= True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='cash_cofig_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='cash_cofig_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='cash_cofig_deleted_by', db_column='deletedBy')


  def __str__(self):
    return "%s cash_config" % self.account
     

  class Meta:
    db_table = "cash_config"
        
