# Generated by Django 4.0.1 on 2022-01-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
