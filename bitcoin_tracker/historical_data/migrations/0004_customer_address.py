# Generated by Django 3.0 on 2020-07-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0003_customer_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
