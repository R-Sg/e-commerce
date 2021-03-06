# Generated by Django 2.2.9 on 2020-02-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200225_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'permissions': (('can_checkout', 'Can checkout'),)},
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='uuid',
            field=models.UUIDField(default=98880627721730, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=61938076132811, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=6700431272805, editable=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='uuid',
            field=models.UUIDField(default=71817688397443, editable=False),
        ),
    ]
