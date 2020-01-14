# Generated by Django 3.0.2 on 2020-01-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koszyk', '0005_auto_20200111_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Zamówienie', 'verbose_name_plural': 'Zamówienia'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(blank=True, choices=[('NOWE', 'Nowe'), ('ZAPISANE', 'Zapisane'), ('WYSŁANE', 'Wysłane'), ('GOTOWE', 'Gotowe'), ('BRAK_MOŻLIWOŚCI_REALIZACJI', 'Brak Możliwości Realizacji'), ('ZREALIZOWANE', 'Zrealizowane'), ('ARCHIWALNE', 'Archiwalne')], default='NOWE', max_length=30),
        ),
    ]