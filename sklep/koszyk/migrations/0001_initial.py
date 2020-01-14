# Generated by Django 2.2.7 on 2019-11-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produkty', '0022_auto_20191130_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ManyToManyField(blank=True, null=True, to='produkty.Produkty')),
            ],
        ),
    ]