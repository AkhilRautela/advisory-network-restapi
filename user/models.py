from django.db import models

import uuid

# Create your models here.


class User(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)


class Booking(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)
    user_id = models.UUIDField()
    advisor_id = models.UUIDField()
    datetime = models.DateTimeField()
