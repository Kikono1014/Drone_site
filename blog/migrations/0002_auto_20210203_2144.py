# Generated by Django 3.1.3 on 2021-02-03 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_photo', models.ImageField(upload_to='blog/static/image/news')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pyblished_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
