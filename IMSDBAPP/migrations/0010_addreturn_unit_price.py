# Generated by Django 4.2.1 on 2023-07-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSDBAPP', '0009_alter_addreturn_return_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addreturn',
            name='unit_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
