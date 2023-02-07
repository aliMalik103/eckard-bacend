from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact
from .tract import Tract

class Project(SoftDeleteModel):
  projectId = models.CharField(max_length=100, unique=True)
  totalNma = models.DecimalField(max_digits=50, decimal_places=10, null=True, blank=True)
  totalRevenue = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
  tract = models.ManyToManyField(Tract, blank=True, related_name= 'tracts', through='TractProject')
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='project_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='project_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='project_deleted_by', db_column='deletedBy')


  def __str__(self):
    return "%s project" % self.projectId
     

  class Meta:
    db_table = "project"
        
