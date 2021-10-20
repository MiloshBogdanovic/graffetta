from django.db import models

# Create your models here.
class OverallInventory(models.Model):
    id = models.AutoField(primary_key=True)
    total_amount_of_work = models.DecimalField(decimal_places=2, max_digits=12)