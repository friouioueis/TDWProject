# Generated by Django 2.2.9 on 2020-01-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Traduction', '0002_auto_20200119_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cv',
            field=models.FileField(null=True, upload_to='files/cvs/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='assertmente',
            field=models.FileField(null=True, upload_to='files/assermente/'),
        ),
    ]
