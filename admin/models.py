from django.db import models
import uuid

# Create your models here.
class Advisor(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
