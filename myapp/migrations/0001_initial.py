# Generated by Django 4.2 on 2023-05-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('job_title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=50)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]