# Generated by Django 4.2.3 on 2023-07-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_map', '0004_persion_detail_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company_name',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]
