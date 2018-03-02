# Generated by Django 2.0 on 2018-03-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180210_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcaprofile',
            name='region',
            field=models.CharField(blank=True, choices=[('NCR', 'National Capital Region'), ('Region I', 'Ilocos Region'), ('CAR', 'Cordillera Administrative Region'), ('Region II', 'Cagayan Valley'), ('Region III', 'Central Luzon'), ('Region IV-A', 'CALABARZON'), ('Region IV-B', 'MIMAROPA'), ('Region V', 'Bicol Region'), ('Region VI', 'Western Visayas'), ('Region VII', 'Central Visayas'), ('Region VIII', 'Eastern Visayas'), ('Region IX', 'Zamboanga Peninsula'), ('Region X', 'Northern Mindanao'), ('Region XI', 'Davao Region'), ('Region XII', 'SOCCSKSARGEN'), ('Region XIII', 'Caraga Region'), ('ARMM', 'Autonomous Region in Muslim Mindanao')], max_length=255, null=True),
        ),
    ]