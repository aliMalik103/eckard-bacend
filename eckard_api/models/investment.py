from .soft_delete_model import SoftDeleteModel, models
from .account import Account
from .project import Project
from .contact import Contact


class Investment(SoftDeleteModel):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  investmentAmount = models.DecimalField(max_digits=50, decimal_places=2)
  acquiredNma = models.DecimalField(max_digits=50, decimal_places=10)
  status = models.CharField(max_length=100, default='active')
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='investment_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='investment_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='investment_deleted_by', db_column='deletedBy')


  def __str__(self):
    return "%s investment" % self.account
     

  class Meta:
    db_table = "investment"
        
