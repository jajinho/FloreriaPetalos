# Generated by Django 2.2.7 on 2019-12-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Petalos', '0006_auto_20191207_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flor',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='flor',
            name='stock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flor',
            name='valor',
            field=models.IntegerField(),
        ),
    ]