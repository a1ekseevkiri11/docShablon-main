# Generated by Django 5.0 on 2024-04-29 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_directionoftraining_supervisoropop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('type1', 'Тип 1'), ('type2', 'Тип 2')], max_length=20)),
                ('pay', models.BooleanField()),
                ('hard_quality', models.TimeField()),
                ('quality', models.TimeField()),
                ('remark', models.TimeField()),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.amount')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
