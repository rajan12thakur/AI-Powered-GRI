import uuid
from django.db import models
from company.models import Company

class Department(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="department")
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
         return self.name
