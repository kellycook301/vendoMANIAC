# Generated by Django 3.0.5 on 2020-04-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendo_matic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
