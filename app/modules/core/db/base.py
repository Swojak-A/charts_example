import uuid

from django.db import models


__all__ = ["BaseModel"]


class BaseModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True
