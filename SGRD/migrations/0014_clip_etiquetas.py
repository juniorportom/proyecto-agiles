# Generated by Django 2.1.2 on 2018-11-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0013_auto_20181103_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='etiquetas',
            field=models.ManyToManyField(blank=True, to='SGRD.Etiqueta'),
        ),
    ]