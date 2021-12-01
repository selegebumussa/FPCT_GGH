# Generated by Django 3.2.7 on 2021-11-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGH', '0007_auto_20211127_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='img/logo/')),
                ('discription', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
