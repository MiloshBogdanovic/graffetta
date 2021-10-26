# Generated by Django 3.2.6 on 2021-10-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_alter_overallinventory_z'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallSituationInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount_of_work', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.DeleteModel(
            name='OverallInventory',
        ),
    ]
