# Generated by Django 4.1.3 on 2022-11-17 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="client_name",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="bills.client",
            ),
            preserve_default=False,
        ),
    ]
