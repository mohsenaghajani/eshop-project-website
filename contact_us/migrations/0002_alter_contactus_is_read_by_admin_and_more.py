# Generated by Django 5.0.2 on 2024-02-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(verbose_name='متن پیام '),
        ),
    ]
