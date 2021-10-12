# Generated by Django 3.2.6 on 2021-10-12 11:01

from django.db import migrations, models
import django.db.models.deletion
import internationalflavor.vat_number.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrationIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title_of_admin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdministrationLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=20)),
                ('company_reg_num', models.IntegerField(unique=True)),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('street', models.CharField(max_length=50)),
                ('street_number', models.CharField(max_length=5)),
                ('cap', models.CharField(max_length=20)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('legal_title_rep', models.CharField(choices=[('SIG.RA', 'SIG.RA'), ('GEOM.', 'GEOM.'), ('RAG.', 'RAG.'), ('ING.', 'ING.'), ('ARCH', 'ARCH'), ('ALTRO', 'ALTRO')], max_length=10, null=True)),
                ('leg_rep_name', models.CharField(max_length=50)),
                ('leg_rep_surname', models.CharField(max_length=50)),
                ('leg_rep_tax_code', models.CharField(max_length=20)),
                ('leg_rep_dob', models.DateField()),
                ('municipal_of_birth_of_leg', models.CharField(max_length=30)),
                ('province_of_birth_of_leg', models.CharField(max_length=30)),
                ('legal_street', models.CharField(max_length=50)),
                ('legal_street_number', models.CharField(max_length=5)),
                ('cap_legal', models.CharField(max_length=30)),
                ('municipal_of_leg_residence', models.CharField(max_length=30)),
                ('province_of_leg_residence', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CondominiumData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('fiscal_code', models.IntegerField()),
                ('street', models.CharField(max_length=50)),
                ('street_number', models.CharField(max_length=5)),
                ('municipality', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('pec_mail', models.EmailField(max_length=254)),
                ('select_administrator', models.CharField(choices=[('Legal', 'Legal'), ('Individual', 'Individual')], max_length=10, null=True)),
                ('admn_individual_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.administrationindividual')),
                ('admn_legal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.administrationlegal')),
            ],
        ),
    ]
