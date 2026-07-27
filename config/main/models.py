from django.db import models


class TransferWindow(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    club = models.CharField(max_length=100)
    transfer_value = models.DecimalField(
        max_digits=18,
        decimal_places=4
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name