# Generated by Django 4.0.3 on 2022-05-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short',
            field=models.CharField(max_length=4),
        ),
    ]
