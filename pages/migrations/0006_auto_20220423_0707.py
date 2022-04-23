# Generated by Django 2.1.1 on 2022-04-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20220415_1648'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bitcoin',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Deposits',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='investment',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='returns',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='twithdraw',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='username',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='withdrawb',
        ),
        migrations.AddField(
            model_name='balance',
            name='Investment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='balance',
            name='Returns',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='balance',
            name='Twithdraw',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='balance',
            name='Withdrawb',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
