# Generated by Django 5.0.6 on 2024-06-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_new_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
    ]
