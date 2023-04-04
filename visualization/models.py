from django.db import models

class Sales(models.Model):
    item = models.CharField(max_length=36)
    price = models.FloatField()

    def __str__(self):
        return f"{self.item} | {self.price}"

    class Meta:
        verbose_name = 'Sales'
