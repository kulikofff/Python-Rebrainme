# Generated by Django 4.0.6 on 2022-07-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbr_srv_side', '0004_remove_server_cpu_remove_server_disk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0', verbose_name='ip_address'),
        ),
    ]