from django.db import models

# Create your models here.
from django.db import models

class Prediction(models.Model):
    tv = models.FloatField()
    radio = models.FloatField()
    newspaper = models.FloatField()
    sales_prediction = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id} - {self.sales_prediction}"
