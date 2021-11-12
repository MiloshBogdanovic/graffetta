# Generated by Django 3.2.6 on 2021-11-12 08:59

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonWorkExVat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt_of_work', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_designer', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_designer', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_coordinator_safety_des', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_coordinator_safety_des', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_coordinator_safety_exe', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_coordinator_safety_exe', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_director_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_director_of_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_director_of_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_thermotechnical', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_thermotechnical', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_thermotechnical', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_energy_expert', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_energy_expert', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_energy_expert', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('poss_respo_work', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('vat_for_respo_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_respo_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('total_tech_exp', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('total_of_the_order', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('vat_for_total_work', models.DecimalField(choices=[(Decimal('0.1'), '10%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.1'), max_digits=10)),
                ('discount_in_invoice', models.DecimalField(blank=True, choices=[(Decimal('0.9'), '90%')], decimal_places=2, default=Decimal('0.9'), max_digits=10)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CommonWorkIncVat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vat_for_total_work', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_of_work', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_of_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges_amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_designer_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_director_of_work', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_director_of_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_thermotechnical', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_thermotechnical_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_energy_expert', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_energy_expert_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('poss_respo_work', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('poss_respo_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_tech_exp', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_tech_exp_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_of_the_order', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_of_the_order_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CommonWorkReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount_includin_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_taxable_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amount_of_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CommonWorkTaxable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_director_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_thermotechnical', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_energy_expert', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('poss_respo_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_tech_exp', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_of_the_order', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OverallExVat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt_of_work', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_designer', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_designer', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_coordinator_safety_des', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_coordinator_safety_des', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_coordinator_safety_exe', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_coordinator_safety_exe', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_director_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_director_of_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_director_of_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_thermotechnical', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_thermotechnical', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_thermotechnical', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_energy_expert', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_energy_expert', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_energy_expert', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('poss_respo_work', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('vat_for_respo_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_respo_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('total_tech_exp', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('total_of_the_order', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('vat_for_total_work', models.DecimalField(choices=[(Decimal('0.1'), '10%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.1'), max_digits=10)),
                ('discount_in_invoice', models.DecimalField(blank=True, choices=[(Decimal('0.9'), '90%')], decimal_places=2, default=Decimal('0.9'), max_digits=10)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OverallIncVat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vat_for_total_work', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_of_work', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_of_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges_amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_designer_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_director_of_work', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_director_of_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_thermotechnical', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_thermotechnical_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_energy_expert', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_energy_expert_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('poss_respo_work', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('poss_respo_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_tech_exp', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_tech_exp_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_of_the_order', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_of_the_order_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OverallReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount_includin_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_taxable_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amount_of_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OverallTaxable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_director_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_thermotechnical', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_energy_expert', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('poss_respo_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_tech_exp', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_of_the_order', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectiveWorkExVat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt_of_work', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_designer', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_designer', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_coordinator_safety_des', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_coordinator_safety_des', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_coordinator_safety_exe', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_coordinator_safety_exe', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_director_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_director_of_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_director_of_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_thermotechnical', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_thermotechnical', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_thermotechnical', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('tech_exp_energy_expert', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('vat_for_energy_expert', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_energy_expert', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('poss_respo_work', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('vat_for_respo_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.22'), max_digits=10)),
                ('ss_cash_for_respo_work', models.DecimalField(choices=[(Decimal('0'), '0%'), (Decimal('0.04'), '4%'), (Decimal('0.05'), '5%')], decimal_places=2, default=Decimal('0.04'), max_digits=10)),
                ('total_tech_exp', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('total_of_the_order', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('vat_for_total_work', models.DecimalField(choices=[(Decimal('0.1'), '10%'), (Decimal('0.22'), '22%')], decimal_places=2, default=Decimal('0.1'), max_digits=10)),
                ('discount_in_invoice', models.DecimalField(blank=True, choices=[(Decimal('0.9'), '90%')], decimal_places=2, default=Decimal('0.9'), max_digits=10)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectiveWorkIncVat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vat_for_total_work', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_of_work', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_of_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_amt_safety_charges_amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_designer_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_director_of_work', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_director_of_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_thermotechnical', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_thermotechnical_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_energy_expert', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('tech_exp_energy_expert_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('poss_respo_work', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('poss_respo_work_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_tech_exp', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_tech_exp_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_of_the_order', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
                ('total_of_the_order_amount_vat', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectiveWorkReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount_includin_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_taxable_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_taxable', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('total_amount_of_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_of_discount_in_invoice_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amount_advance_deposit_by_customer_vat', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectiveWorkTaxable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amt_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_amt_safety_charges', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_designer', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_des', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_coordinator_safety_exe', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_director_of_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_thermotechnical', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('tech_exp_energy_expert', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('poss_respo_work', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_tech_exp', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_of_the_order', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TableContract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('common_ex_vat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.commonworkexvat')),
                ('common_in_vat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.commonworkincvat')),
                ('common_rep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.commonworkreport')),
                ('common_taxable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.commonworktaxable')),
                ('overall_ex_vat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.overallexvat')),
                ('overall_in_vat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.overallincvat')),
                ('overall_rep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.overallreport')),
                ('overall_taxable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.overalltaxable')),
                ('subjective_ex_vat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.subjectiveworkexvat')),
                ('subjective_in_vat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.subjectiveworkincvat')),
                ('subjective_rep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.subjectiveworkreport')),
                ('subjective_taxable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.subjectiveworktaxable')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
