# Generated by Django 3.1.3 on 2021-02-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210203_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
