# Generated by Django 3.2.8 on 2021-11-26 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(default='', max_length=110)),
                ('cust_no', models.CharField(default='', max_length=13, unique=True)),
                ('addr', models.TextField(default='', max_length=500)),
                ('del_addr', models.TextField(default='', max_length=500)),
                ('tot_amt', models.IntegerField(blank=True, default=0)),
                ('pay_status', models.CharField(choices=[('paid', 'Paid'), ('notpaid', 'Not Paid')], default='paid', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InvoiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='', max_length=110)),
                ('quty', models.IntegerField(blank=True, default=0)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('net_amt', models.IntegerField(blank=True, default=0)),
                ('invoice', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='inv_dtl', to='jinjatemp.invoice')),
            ],
        ),
    ]
