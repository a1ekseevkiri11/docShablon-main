# Generated by Django 5.0 on 2024-05-03 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_delete_supervisorpracticeproductiontasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.group')),
                ('practice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.practice')),
            ],
        ),
    ]