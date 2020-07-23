# Generated by Django 3.0 on 2020-07-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0005_customer_color_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
