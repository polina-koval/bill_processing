from django.contrib import admin

from bills.models import Bill, Client, Organization, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["title", "client"]


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["number", "bill_sum", "date", "get_services"]

    def get_services(self, obj):
        return "\n".join([service.title for service in obj.services.all()])
