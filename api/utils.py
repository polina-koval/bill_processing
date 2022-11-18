from datetime import datetime

from django.db import transaction

from bills.models import Bill, Client, Organization, Service


def validate_client(client_name: str) -> Client:
    if client_name:
        client, _ = Client.objects.get_or_create(name=client_name)
        return client
    raise ValueError("No client name")


def validate_organization(org_name: str, client: Client) -> Organization:
    if org_name:
        org, _ = Organization.objects.get_or_create(
            title=org_name, client=client
        )
        return org
    raise ValueError("No client organization")


def validate_bill_sum(bill_sum: str) -> float:
    try:
        bill_sum = float(bill_sum.replace(",", "."))
        return bill_sum
    except ValueError:
        raise ValueError("sum field must be a number")


def validate_date(date_str: str) -> datetime:
    try:
        date = datetime.strptime(date_str, "%d.%m.%Y")
        return date
    except ValueError:
        raise ValueError("Invalid date format")


def is_unique_bill(client: Client, org: Organization, number: str) -> bool:
    bills = Bill.objects.filter(
        client_name=client,
        client_name__organizations__title=org,
        number=number,
    )
    if bills.count() == 0:
        return True
    return False


@transaction.atomic()
def save_bill(data: dict) -> dict:
    client = validate_client(data["client_name"])
    org = validate_organization(data["client_org"], client)
    number = data["№"]
    if not is_unique_bill(client, org, number):
        raise ValueError(
            f"Bill number {number} already exists for a {client} from an {org}."
        )
    bill_sum = validate_bill_sum(data["sum"])
    date = validate_date(data["date"])
    bill = Bill.objects.create(
        client_name=client, number=number, bill_sum=bill_sum, date=date
    )
    services = data["service"]
    if services not in ("", "-"):
        for service in services.split(";"):
            obj, _ = Service.objects.get_or_create(title=service)
            bill.services.add(obj)
        bill.save()
    else:
        raise ValueError("Services not listed")
    return data
