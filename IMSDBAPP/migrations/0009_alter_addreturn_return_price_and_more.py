# Generated by Django 4.2.1 on 2023-07-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSDBAPP', '0008_alter_addsale_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addreturn',
            name='return_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addreturn',
            name='return_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addsale',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addsale',
            name='unit_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]