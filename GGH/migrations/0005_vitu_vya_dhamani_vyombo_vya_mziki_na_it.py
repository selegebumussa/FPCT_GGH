# Generated by Django 3.2.7 on 2021-11-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGH', '0004_auto_20211030_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitu_vya_dhamani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viti', models.IntegerField()),
                ('meza', models.IntegerField()),
                ('stuli', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vyombo_vya_mziki_na_IT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera', models.IntegerField()),
                ('computer', models.IntegerField()),
                ('gitaa', models.IntegerField()),
                ('drams', models.IntegerField()),
                ('microphone', models.IntegerField()),
                ('speaker', models.IntegerField()),
                ('vinanda', models.IntegerField()),
            ],
        ),
    ]
