# Generated by Django 4.2.1 on 2023-07-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSDBAPP', '0006_remove_addsale_code_addreturn_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addsale',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]