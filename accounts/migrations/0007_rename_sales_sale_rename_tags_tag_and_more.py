# Generated by Django 5.0.7 on 2024-07-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_order_customer_remove_order_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]