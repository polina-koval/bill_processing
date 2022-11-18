from rest_framework import serializers

from bills.models import Bill, Service, Client


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["title"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name"]


class BillSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Bill
        fields = ["client_name", "number", "bill_sum", "date", "services"]


class UploadBillSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ["file"]
