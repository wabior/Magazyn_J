# Generated by Django 3.0.2 on 2020-01-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0003_auto_20200119_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='numer',
            field=models.IntegerField(blank=True, default=1930815392, null=True),
        ),
    ]
