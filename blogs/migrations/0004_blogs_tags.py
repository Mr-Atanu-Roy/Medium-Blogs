# Generated by Django 4.0.6 on 2022-07-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blogs_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='tags',
            field=models.CharField(default=None, max_length=355),
        ),
    ]