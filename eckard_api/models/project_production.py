from .soft_delete_model import SoftDeleteModel, models
from .contact import Contact
from .project import Project

class ProjectProduction(SoftDeleteModel):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  date = models.DateField()
  gas = models.DecimalField(max_digits=12, decimal_places=5)
  oil = models.DecimalField(max_digits=12, decimal_places=5)
  createdAt = models.DateTimeField(auto_now_add=True, null= True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null= True, blank=True)
  createdBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='project_production_created_by', db_column='createdBy')
  updatedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='project_production_updated_by', db_column='updatedBy')
  deletedBy = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, related_name='project_production_deleted_by', db_column='deletedBy')


  class Meta:
    db_table = "project_production"
        
