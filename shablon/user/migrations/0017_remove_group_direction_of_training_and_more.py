# Generated by Django 5.0 on 2024-05-02 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_practicestudent_production_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='direction_of_training',
        ),
        migrations.AddField(
            model_name='group',
            name='direction_of_training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.directionoftraining'),
        ),
    ]