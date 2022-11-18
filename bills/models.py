from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=255)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="organizations"
    )

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

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

    class Meta:
        verbose_name = "Bill"
        verbose_name_plural = "Bills"

    def __str__(self):
        return str(self.number)
