# Generated by Django 3.1 on 2020-08-12 10:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(default='', max_length=256, verbose_name='First Name')),
                ('last_name', models.CharField(default='', max_length=256, verbose_name='Last Name')),
                ('position', models.CharField(default='', max_length=256, verbose_name='Position')),
                ('role', models.CharField(choices=[('', 'Lack of information'), ('board', 'Board'), ('guide', 'Guide'), ('maintenance', 'Maintenance'), ('researcher', 'Researcher')], default='', max_length=256, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ('-created_at',),
            },
        ),
    ]
