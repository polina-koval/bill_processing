from django.urls import path
from rest_framework import routers

from api.views import BillViewSet, UploadBillViewSet

router = routers.DefaultRouter()
router.register(r"bills", BillViewSet, basename="bill")

urlpatterns = router.urls

urlpatterns += [
    path("upload-bill/", UploadBillViewSet.as_view(), name="upload-bill"),
]
