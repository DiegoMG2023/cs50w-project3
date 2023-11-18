# Generated by Django 4.2.7 on 2023-11-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True)),
            ],
        ),
    ]