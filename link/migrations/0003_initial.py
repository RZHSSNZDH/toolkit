# Generated by Django 4.0.3 on 2022-05-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('link', '0002_delete_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.CharField(max_length=200)),
                ('short', models.CharField(max_length=4, null=True)),
            ],
        ),
    ]