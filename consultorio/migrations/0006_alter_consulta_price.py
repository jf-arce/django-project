# Generated by Django 5.1.4 on 2024-12-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0005_rename_medicamentexpaciente_medicamentoxpaciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='price',
            field=models.DecimalField(decimal_places=2, default=4000.0, max_digits=10),
        ),
    ]
