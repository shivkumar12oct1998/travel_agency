# Generated by Django 5.1.2 on 2024-11-22 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus1', '0002_rename_name_usersideinfo_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersideinfo',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus1.adminsidedetail'),
        ),
    ]
