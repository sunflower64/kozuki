# Generated by Django 4.0.4 on 2022-06-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_producto_tipoanimal_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipoanimal_producto',
            field=models.IntegerField(null=True),
        ),
    ]
