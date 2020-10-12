from django.db import models

class RideDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()

    def __str__(self):
        return str(self.user_id)