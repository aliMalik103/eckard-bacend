from .soft_delete_model import SoftDeleteModel, models
from .listing import Listing
from .offer import Offer
from .contact import Contact


class ListingOffer(SoftDeleteModel):
  offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='listings')
  listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='offers')
  acceptedOffer = models.BooleanField(default=False, blank=True)


  class Meta:
    db_table = "listing_offer"
        
