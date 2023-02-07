from .soft_delete_model import SoftDeleteModel, models
from .status import Status
from .contact import Contact
from .constraint import Constraint


class Offer(SoftDeleteModel):
  status = models.ForeignKey(Status, on_delete=models.PROTECT)
  offerAmount = models.DecimalField(max_digits=9, decimal_places=2)
  constraints = models.ManyToManyField(Constraint, blank=True)
  contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
  comments = models.CharField(max_length=2000, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='offer_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='offer_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='offer_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "offer"

