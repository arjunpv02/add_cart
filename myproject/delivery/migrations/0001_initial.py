# Generated by Django 5.0.6 on 2024-06-21 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0003_alter_customer_phone'),
        ('orders', '0003_alter_order_order_status'),
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('delivery_address', models.TextField()),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='customers.customer')),
                ('order_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='orders.orderitem')),
                ('product', models.ManyToManyField(related_name='deliveries', to='products.product')),
            ],
        ),
    ]
