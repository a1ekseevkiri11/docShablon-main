# Generated by Django 5.0 on 2024-05-03 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_reportgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directionoftraining',
            name='institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.institute'),
        ),
        migrations.RemoveField(
            model_name='directionoftraining',
            name='supervisorOPOP',
        ),
        migrations.AddField(
            model_name='directionoftraining',
            name='supervisorOPOP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.supervisoropop'),
        ),
    ]
