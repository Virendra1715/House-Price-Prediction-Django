from django.db import models
from django.contrib.auth.models import User


class HousePrediction(models.Model):
    bedrooms = models.FloatField()
    bathrooms = models.FloatField()
    sqft_living = models.FloatField()
    sqft_lot = models.FloatField()
    floors = models.FloatField()
    condition = models.FloatField()
    grade = models.FloatField()
    sqft_above = models.FloatField()
    sqft_basement = models.FloatField()
    yr_built = models.FloatField()
    yr_renovated = models.FloatField()
    sqft_living15 = models.FloatField()
    sqft_lot15 = models.FloatField()
    predicted_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return f"Prediction #{self.pk}"

 