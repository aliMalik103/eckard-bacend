from .soft_delete_model import SoftDeleteModel, models
from .listing_type import ListingType
from .status import Status
from .auction_type import AuctionType
from .account import Account
from .project import Project
from .offer import Offer
from .contact import Contact
from .constraint import Constraint
import uuid

class Listing(SoftDeleteModel):
  listing_type = models.ForeignKey(ListingType, on_delete=models.PROTECT)
  status = models.ForeignKey(Status, on_delete=models.PROTECT)
  listingName = models.CharField(max_length=100)
  listingStart = models.DateTimeField()
  auction_type = models.ForeignKey(AuctionType, on_delete=models.PROTECT)
  auctionEnd = models.DateTimeField()
  constraints = models.ManyToManyField(Constraint, blank=True)
  comments = models.CharField(max_length=2000, null=True, blank=True)
  account = models.ForeignKey(Account, on_delete=models.PROTECT)
  project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
  nma = models.DecimalField(max_digits=50, decimal_places=6, null=True, blank=True)
  minimumAsk = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
  buyNowPrice = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
  directSaleToken = models.UUIDField(default=uuid.uuid4, null=True, blank=True, unique=True)
  offer = models.ManyToManyField(Offer, related_name='offers', blank=True, through='ListingOffer')
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='listing_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='listing_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='listing_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "listing"

