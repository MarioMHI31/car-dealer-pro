# Generated by Django 5.1.7 on 2025-03-20 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('Mercedes', 'Mercedes'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Opel', 'Opel'), ('Renault', 'Renault'), ('Peugeot', 'Peugeot'), ('Hyundai', 'Hyundai')], default='BMW', max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mileage', models.IntegerField()),
                ('engine', models.CharField(max_length=100)),
                ('horsepower', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=20)),
                ('car_body', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Cabrio', 'Cabrio'), ('Pickup', 'Pickup'), ('Break', 'Break'), ('Minivan', 'Minivan'), ('Sport', 'Sport')], default='Sedan', max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to='car_images/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_images', to='main.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='car_images', to='main.carimage'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
