# Generated by Django 4.0.6 on 2022-08-22 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_rename_amount_loan_amount_rename_date_loan_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='amount',
            new_name='loan_amount',
        ),
    ]
