# Generated by Django 4.0.1 on 2022-05-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default=90, max_length=90),
            preserve_default=False,
        ),
    ]