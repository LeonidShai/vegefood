# Generated by Django 3.0.4 on 2020-04-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_auto_20200410_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enproduct',
            name='discount',
            field=models.IntegerField(blank=True, default=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ruproduct',
            name='discount',
            field=models.IntegerField(blank=True, default=8),
            preserve_default=False,
        ),
    ]
