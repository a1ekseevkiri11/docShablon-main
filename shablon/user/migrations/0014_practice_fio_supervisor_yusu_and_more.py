# Generated by Django 5.0 on 2024-05-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_practice_number_decree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='fio_supervisor_YuSU',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='fio_supervisor_company',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='post_supervisor_YuSU',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='post_supervisor_company',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='practice',
            name='adress_place',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='practice',
            name='title_place',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
