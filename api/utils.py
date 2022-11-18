from datetime import datetime

from bills.models import Bill, Client, Organization, Service


def save_bill(data):
    client, _ = Client.objects.get_or_create(name=data["client_name"])
    org, _ = Organization.objects.get_or_create(
        title=data["client_org"], client=client
    )
    number = data["№"]
    bill_sum = float(data["sum"].replace(",", "."))
    date = datetime.strptime(data["date"], "%d.%m.%Y")
    bill = Bill.objects.create(
        client_name=client, number=number, bill_sum=bill_sum, date=date
    )
    for service in data["service"].split(";"):
        obj, _ = Service.objects.get_or_create(title=service)
        bill.services.add(obj)
    bill.save()
    return data
