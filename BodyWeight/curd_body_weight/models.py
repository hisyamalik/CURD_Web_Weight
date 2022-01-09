from django.db import models

# Create your models here.
class modelBodyWeight(models.Model):
    tanggal = models.DateField()
    max_val = models.IntegerField()
    min_val = models.IntegerField()

    class Meta:
        db_table = 'bodyweight'