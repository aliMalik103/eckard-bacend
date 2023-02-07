from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact


class AuctionType(SoftDeleteModel):
  auctionType = models.CharField(max_length=100)
  auctionLabel= models.CharField(max_length=100, null= True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='auction_type_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='auction_type_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='auction_type_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "auction_type"

