from .soft_delete_model import SoftDeleteModel, models
from .project import Project
from .tract import Tract
from .contact import Contact


class TractProject(models.Model):
  tract = models.ForeignKey(Tract, on_delete=models.CASCADE, related_name='projects')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tracts')
  nmaInProject = models.DecimalField(max_digits=50, decimal_places=10)


  class Meta:
    db_table = "tract_project"
        
