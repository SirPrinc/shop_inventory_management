# Generated by Django 5.0.7 on 2024-07-24 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_sales_sale_rename_tags_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
