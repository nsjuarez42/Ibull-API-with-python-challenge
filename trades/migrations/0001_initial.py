# Generated by Django 3.1.3 on 2022-01-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=4)),
                ('user_id', models.IntegerField()),
                ('symbol', models.CharField(max_length=3)),
                ('shares', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('timestamp', models.BigIntegerField()),
            ],
        ),
    ]
