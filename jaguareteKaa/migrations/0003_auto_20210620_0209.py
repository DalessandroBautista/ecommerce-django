# Generated by Django 3.2.4 on 2021-06-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaguareteKaa', '0002_auto_20210620_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
