# Generated by Django 4.0.3 on 2022-04-06 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name of Category: ')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='Coupon Name')),
                ('discount', models.FloatField(default=0, max_length=40, verbose_name='Discount Percent')),
            ],
            options={
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name of Product')),
                ('shape', models.CharField(choices=[('rectangle', 'Rectangle'), ('rounded', 'Rounded')], default='rectangle', max_length=20)),
                ('finish', models.CharField(choices=[('matt', 'Matt'), ('gloss', 'Gloss'), ('non lamination', 'Non Lamination')], default='matt', max_length=20)),
                ('quality', models.CharField(choices=[('standard', 'Standard'), ('premium', 'Premium')], default='premium', max_length=20)),
                ('thickness', models.CharField(choices=[('250 GSM', '250 GSM'), ('300 GSM', '300 GSM')], default='250 GSM', max_length=20)),
                ('price', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='catagories', to='vcardApp.categorymodel')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('ord_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ord_quantity', models.IntegerField(default=0)),
                ('ord_price', models.FloatField(default=0.0)),
                ('ord_date', models.DateTimeField(auto_now_add=True)),
                ('ord_status', models.CharField(default='Pending', max_length=50)),
                ('ord_feedback', models.TextField(blank=True, null=True)),
                ('ord_image', models.FileField(blank=True, null=True, upload_to='order/customised_images/')),
                ('cancellation_status', models.CharField(default='No', max_length=50)),
                ('cancellation_date', models.DateTimeField(blank=True, null=True)),
                ('cancellation_reason', models.TextField(blank=True, default='None')),
                ('user_gst_num', models.CharField(blank=True, default='Not Provided', max_length=100)),
                ('user_refund_cheque', models.FileField(blank=True, upload_to='order/OrderRefund/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcardApp.productmodel')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
