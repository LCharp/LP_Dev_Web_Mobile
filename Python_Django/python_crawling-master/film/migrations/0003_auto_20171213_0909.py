# Generated by Django 2.0 on 2017-12-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20171211_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='AnneeSortie',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='film',
            name='sortie',
            field=models.CharField(max_length=230),
        ),
    ]