# Generated by Django 3.2.4 on 2021-06-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaguareteKaa', '0003_auto_20210620_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]