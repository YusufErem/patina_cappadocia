# Generated by Django 5.1.2 on 2024-12-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('royal', 'Royal Oda'), ('exclusive', 'Exclusive Oda'), ('luxury', 'Luxury Oda'), ('executive', 'Executive Oda'), ('superior', 'Superior Oda')], max_length=10),
        ),
    ]
