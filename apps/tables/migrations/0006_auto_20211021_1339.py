# Generated by Django 3.2.6 on 2021-10-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_auto_20211020_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount_includin_vat', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount_of_discount_in_invoice', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_taxable_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount_of_discount_in_invoice_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amount_of_vat', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount_of_discount_in_invoice_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='OverallSituationInventory',
        ),
    ]
