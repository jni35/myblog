# Generated by Django 4.0 on 2021-12-31 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images/%y/%m/%d/'),
        ),
    ]
