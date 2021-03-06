# Generated by Django 3.1 on 2020-08-12 10:53

from django.db import migrations, models
import django.db.models.deletion
import modules.plotly_go_vs_express.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('plotly_go_vs_express', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YearRoundEmployerExpenses',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('year', models.PositiveIntegerField(default=modules.plotly_go_vs_express.models.current_year, verbose_name='Fiscal Year')),
                ('value', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Value')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_expenses', to='plotly_go_vs_express.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Employer Expenses',
                'verbose_name_plural': 'Employer Expenses',
                'ordering': ('-created_at',),
            },
        ),
    ]
