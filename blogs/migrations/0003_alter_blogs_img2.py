# Generated by Django 4.0.6 on 2022-07-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogs_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='img2',
            field=models.FileField(default=None, max_length=500, null=True, upload_to='blog_images/'),
        ),
    ]