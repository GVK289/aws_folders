# Generated by Django 3.0 on 2020-07-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
