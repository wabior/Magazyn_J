# Generated by Django 3.0.2 on 2020-01-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0002_remove_produkty_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='numer',
            field=models.IntegerField(blank=True, default=1930815377, null=True),
        ),
    ]
