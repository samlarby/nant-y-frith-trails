# Generated by Django 3.2.25 on 2024-09-15 13:46

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20240914_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='strips_pid',
            new_name='stripe_pid',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
