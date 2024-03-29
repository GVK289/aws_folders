# Generated by Django 3.0 on 2020-07-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('total_btc', models.IntegerField(default=0)),
            ],
        ),
    ]
