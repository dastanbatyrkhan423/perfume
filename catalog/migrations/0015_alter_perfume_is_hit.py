# Generated by Django 5.1.7 on 2025-03-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_perfume_is_hit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='is_hit',
            field=models.BooleanField(default=False, verbose_name='Хит продаж'),
        ),
    ]
