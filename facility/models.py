# from django.db import models
# import uuid
# class Facility(models.Model):
#     id= models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     company=models.ForeignKey("company.Company", on_delete=models.CASCADE,related_name="facilities")
#     org_unit=models.ForeignKey("organisationunit.orgnisationUnit",on_delete=models.CASCADE,related_name="facilities")
#     name=models.CharField(max_length=255)
#     facility_type=models.CharField(max_length=100)
#     address=models.TextField()
#     is_active=models.BooleanField(default=True)

#     def __str__(self):
#         return self.name    
