# Generated by Django 4.0.4 on 2022-06-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion_producto',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
