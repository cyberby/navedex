from datetime import date

from django.contrib.auth.models import User
from django.db import models, DEFAULT_DB_ALIAS


class Project(models.Model):
    name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Naver(models.Model):
    name = models.CharField(max_length=255, null=False)
    birthdate = models.DateField(null=True, default=date.today)
    admission_date = models.DateField(null=True)
    job_role = models.CharField(max_length=255, null=False)
    projects = models.ManyToManyField(Project, related_name='navers', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)