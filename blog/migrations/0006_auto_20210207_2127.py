# Generated by Django 3.1.3 on 2021-02-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210207_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/image/'),
        ),
    ]