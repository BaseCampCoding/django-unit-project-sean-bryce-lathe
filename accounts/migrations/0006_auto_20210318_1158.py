# Generated by Django 3.1.7 on 2021-03-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210316_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_image'),
        ),
    ]
