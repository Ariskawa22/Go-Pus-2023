# Generated by Django 3.0 on 2021-07-02 17:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20210703_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukuinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2030cff8-4ba9-47df-a386-132dcea34311'), primary_key=True, serialize=False),
        ),
    ]
