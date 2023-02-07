from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact
from django.contrib.postgres.fields import CICharField


class Account(SoftDeleteModel):
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
  accountId = models.CharField(max_length=100, unique=True)
  accountName = models.CharField(max_length=100)
  notes = models.CharField(max_length=100, null=True, blank=True)
  accountStatus = models.CharField(max_length=100)
  mpStatus = models.CharField(max_length=100, null=True)
  mpName = CICharField(max_length=50, unique=True, null=True)  
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='account_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='account_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='account_deleted_by', db_column='deletedBy')


  def __str__(self):
    return "%s account" % self.accountName
     

  class Meta:
    db_table = "account"
        
