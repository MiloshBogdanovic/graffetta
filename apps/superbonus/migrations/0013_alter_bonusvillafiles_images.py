# Generated by Django 3.2.6 on 2022-02-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superbonus', '0012_alter_bonusvillafiles_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusvillafiles',
            name='images',
            field=models.ImageField(blank=True, upload_to='staticfiles/villa/img/'),
        ),
    ]
