# Generated by Django 2.1.3 on 2018-11-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rewards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
