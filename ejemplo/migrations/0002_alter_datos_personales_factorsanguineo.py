# Generated by Django 4.1.3 on 2022-12-12 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Datos_Personales',
            name='FactorSanguineo',
            field=models.CharField(max_length=100),
        ),
    ]
