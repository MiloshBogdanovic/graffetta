# Generated by Django 3.2.6 on 2021-10-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_auto_20211021_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonworkexvat',
            name='ss_cash_for_tech_exp',
            field=models.DecimalField(choices=[(0, '0%'), (0.04, '4%'), (0.05, '5%')], decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='commonworktaxable',
            name='total_amt_of_work',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='overallexvat',
            name='ss_cash_for_tech_exp',
            field=models.DecimalField(choices=[(0, '0%'), (0.04, '4%'), (0.05, '5%')], decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='overalltaxable',
            name='total_amt_of_work',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='subjectiveworkexvat',
            name='ss_cash_for_tech_exp',
            field=models.DecimalField(choices=[(0, '0%'), (0.04, '4%'), (0.05, '5%')], decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='subjectiveworktaxable',
            name='total_amt_of_work',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
