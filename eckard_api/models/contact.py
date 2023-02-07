from .soft_delete_model import SoftDeleteModel, models


class Contact(SoftDeleteModel):
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  email = models.EmailField(max_length=255)
  password = models.CharField(max_length=100)
  mpStatus = models.CharField(max_length=100)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='contact_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='contact_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='contact_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "contact"

