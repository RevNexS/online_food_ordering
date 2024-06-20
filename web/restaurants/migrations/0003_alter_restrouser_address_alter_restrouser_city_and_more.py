# Generated by Django 5.0.4 on 2024-06-14 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_restrouser_desc_alter_restrouser_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrouser',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='contact_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='images_path',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='menu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restromenu'),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='street',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='restrouser',
            name='timing',
            field=models.CharField(max_length=100, null=True),
        ),
    ]