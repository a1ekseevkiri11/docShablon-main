# Generated by Django 5.0 on 2024-04-29 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisorOPOP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('adress', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('type', models.CharField(choices=[('type1', 'Тип 1'), ('type2', 'Тип 2')], max_length=20)),
                ('kind', models.CharField(choices=[('kind1', 'Вид 1'), ('kind2', 'Вид 2')], max_length=20)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('number_decree', models.CharField(choices=[('kind1', 'Вид 1'), ('kind2', 'Вид 2')], max_length=20)),
                ('date_decree', models.DateField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supervisorOPOP.place')),
            ],
        ),
    ]
