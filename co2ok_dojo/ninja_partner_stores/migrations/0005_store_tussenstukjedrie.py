# Generated by Django 2.1.5 on 2019-01-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_partner_stores', '0004_auto_20181207_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='tussenstukjedrie',
            field=models.CharField(default='', max_length=200),
        ),
    ]