import io

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
import csv

from api.serializers import BillSerializer, UploadBillSerializer
from api.utils import save_bill
from bills.models import Bill

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["client_name", "client_name__organizations"]


class UploadBillViewSet(generics.CreateAPIView):
    serializer_class = UploadBillSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file'].read().decode('utf-8')
        text = csv.DictReader(io.StringIO(file))
        for row in text:
            save_bill(row)
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

