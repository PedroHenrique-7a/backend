# Generated by Django 5.1.2 on 2024-11-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20241129_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]