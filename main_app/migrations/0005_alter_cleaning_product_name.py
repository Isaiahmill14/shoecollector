# Generated by Django 5.0.3 on 2024-04-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cleaning_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning_product',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
