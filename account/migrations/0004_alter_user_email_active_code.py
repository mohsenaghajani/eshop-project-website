# Generated by Django 5.0.2 on 2024-03-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_active_code',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='کد فعال سازی ایمیل'),
        ),
    ]
