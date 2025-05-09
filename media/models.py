from django.db import models


class ImageHash(models.Model):
    # Can use this as the path for now since its unique (will also keep everything in 1 directory for now)
    img_hash = models.CharField(max_length=32, unique=True)

    # Can use as common name for now; unsure if needed in the future; duplicates allowed
    filename = models.TextField(default=None, null=True)