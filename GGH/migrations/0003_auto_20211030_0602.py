# Generated by Django 3.2.7 on 2021-10-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGH', '0002_auto_20211030_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washirika',
            name='jinsia',
            field=models.CharField(choices=[('Me', 'Mwanaume'), ('Ke', 'Mwanamke')], max_length=2),
        ),
        migrations.AlterField(
            model_name='washirika',
            name='namba_ya_simu',
            field=models.IntegerField(),
        ),
    ]