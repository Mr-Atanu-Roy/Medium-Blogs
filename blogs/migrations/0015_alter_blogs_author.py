# Generated by Django 4.0.6 on 2022-07-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_blogs_authorimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='author',
            field=models.CharField(default='Atanu', max_length=255),
        ),
    ]