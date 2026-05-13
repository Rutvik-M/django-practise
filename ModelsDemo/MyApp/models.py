from django.db import models

class Course(models.Model):
    cname=models.CharField(max_length=100)
    duration=models.IntegerField()
    fees_details=models.FloatField(default=20000)

    class Meta:
        db_table='Course'


class Trainer(models.Model):
    tname=models.CharField(max_length=50)
    tid=models.IntegerField()
    tfee=models.FloatField(default =10000)

    class Meta:
        db_table='Trainer'


