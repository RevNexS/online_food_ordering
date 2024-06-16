# Generated by Django 5.0.4 on 2024-06-12 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestroMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='RestroUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('images_path', models.ImageField(upload_to='images/')),
                ('timing', models.CharField(max_length=100)),
                ('stars', models.IntegerField()),
                ('desc', models.TextField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='restro_user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restromenu')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='restro_user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RestroMenuImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/menu_img')),
                ('restro_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restaurants.restrouser')),
            ],
        ),
        migrations.AddField(
            model_name='restromenu',
            name='restro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restrouser'),
        ),
    ]
