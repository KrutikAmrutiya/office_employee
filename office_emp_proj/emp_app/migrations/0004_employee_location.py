# Generated by Django 4.2.7 on 2023-12-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_delete_department_delete_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.CharField(default='', max_length=30),
        ),
    ]