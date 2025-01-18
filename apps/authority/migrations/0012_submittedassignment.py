# Generated by Django 5.1.3 on 2025-01-16 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0011_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittedAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='assignment/')),
                ('is_graded', models.BooleanField(blank=True, default=False, null=True)),
                ('grade', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_assignment', to='authority.assignment')),
                ('submitted_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_assignment', to='authority.enrolledstudent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
