# Generated by Django 4.0 on 2021-12-27 23:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[0-9]{3,} [A-Za-z]{3,} [Az-az{3,}]$', 'Use format: street number + street name')])),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('house_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='homeowners.house')),
            ],
        ),
    ]
