# Generated by Django 5.0.2 on 2024-03-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0008_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='حذف شده / نشده'),
        ),
    ]