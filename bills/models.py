from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=255)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="organizations"
    )

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Bill(models.Model):
    client_name = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="bils"
    )
    number = models.IntegerField()
    bill_sum = models.FloatField()
    date = models.DateField()
    services = models.ManyToManyField("Service")

    def __str__(self):
        return str(self.number)
