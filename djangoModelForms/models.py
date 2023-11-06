from __future__ import unicode_literals
from django.db import models
class HpStudents(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=20)
    mobile=models.IntegerField()

    class Meta:
        db_table="hpclass"