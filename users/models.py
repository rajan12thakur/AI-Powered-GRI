import uuid

from django.db import models
from company.models import Company


class UserAccount(models.Model):
    class Status(models.TextChoices):
         ACTIVE = "active", "Active"
         INACTIVE = "inactive", "Inactive"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="users"
    )

    full_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    password_hash = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    is_company_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Role(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name