# Generated by Django 4.2.3 on 2023-07-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persion_detail',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
