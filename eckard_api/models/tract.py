from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact


class Tract(SoftDeleteModel):
  tractId = models.CharField(max_length=20, unique=True)
  township = models.CharField(max_length=20)
  range = models.CharField(max_length=20)
  section = models.CharField(max_length=20)
  country = models.CharField(max_length=20)
  state = models.CharField(max_length=20)
  royalityInterest = models.DecimalField(max_digits=50, decimal_places=2)
  costPerNma = models.DecimalField(max_digits=50, decimal_places=2)
  totalNma = models.DecimalField(max_digits=50, decimal_places=10)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='tract_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='tract_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='tract_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "tract"
        
