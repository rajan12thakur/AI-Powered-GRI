# Create your models here.
import uuid

from django.db import models
from company.models import Company

class OrganizationUnit(models.Model):
    UNIT_TYPES = [
        ("division", "Division"),
        ("department", "Department"),
        ("team", "Team"),
        ("branch", "Branch"),
        ("other", "Other"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="organization_units",
    )
    parent_unit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    name = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=50, choices=UNIT_TYPES)
    country = models.CharField(max_length=2)
    ownership_pct = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name