# Generated by Django 5.0.6 on 2024-06-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_new_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]