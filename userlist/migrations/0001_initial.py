# Generated by Django 5.0.2 on 2024-02-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.IntegerField(max_length=3)),
                ('identificacion', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
            ],
        ),
    ]