from datetime import datetime

from bills.models import Bill, Client, Organization, Service


def save_bill(data):
    if data["client_name"]:
        client, _ = Client.objects.get_or_create(name=data["client_name"])
    else:
        raise ValueError("No client name")
    if data["client_org"]:
        org, _ = Organization.objects.get_or_create(
        title=data["client_org"], client=client
    )
    else:
        raise ValueError(("No client organization"))
    number = data["№"]
    try:
        bill_sum = float(data["sum"].replace(",", "."))
    except ValueError:
        raise ValueError("sum field must be a number")
    try:
        date = datetime.strptime(data["date"], "%d.%m.%Y")
    except ValueError:
        raise ValueError("Invalid date format")
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
