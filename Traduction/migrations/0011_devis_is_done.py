# Generated by Django 2.2.9 on 2020-01-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Traduction', '0010_devis_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis',
            name='is_done',
            field=models.BooleanField(default=True),
        ),
    ]
