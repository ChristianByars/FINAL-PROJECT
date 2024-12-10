# Generated by Django 5.1.3 on 2024-12-08 21:43

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
                ('cat_username', models.CharField(max_length=20)),
                ('birthday_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birthday', birthday.fields.BirthdayField()),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_first_name', models.CharField(max_length=30)),
                ('human_last_name', models.CharField(max_length=30)),
                ('cat_username', models.CharField(max_length=20)),
                ('birthday_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birthday', birthday.fields.BirthdayField()),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
