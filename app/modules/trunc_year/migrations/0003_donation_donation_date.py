# Generated by Django 3.0.8 on 2020-08-03 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trunc_year', '0002_donation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Donation Date'),
        ),
    ]
