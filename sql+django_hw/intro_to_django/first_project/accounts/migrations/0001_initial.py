# Generated by Django 4.0 on 2021-12-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('session_token', models.IntegerField()),
            ],
        ),
    ]
