# Generated by Django 5.0.6 on 2024-06-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_new_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_user',
            name='image',
            field=models.ImageField(default=1, upload_to='product_image/'),
            preserve_default=False,
        ),
    ]
