# Generated by Django 5.0.2 on 2024-03-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(null=True, verbose_name='تلفن همراه'),
        ),
    ]
