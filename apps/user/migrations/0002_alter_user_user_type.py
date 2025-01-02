# Generated by Django 5.1.3 on 2024-12-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')], default='admin', editable=False, max_length=15, null=True, verbose_name='User Type'),
        ),
    ]