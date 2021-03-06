# Generated by Django 4.0.4 on 2022-05-23 18:35

from django.db import migrations, models
import user_info.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_image',
            field=models.ImageField(blank=True, default=user_info.models.get_default_profile_image, max_length=255, null=True, upload_to='', verbose_name='大頭照'),
        ),
    ]
