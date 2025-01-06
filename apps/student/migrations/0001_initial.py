# Generated by Django 5.1.3 on 2025-01-04 16:06

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authority', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guardian_name', models.CharField(blank=True, max_length=150, null=True)),
                ('relation_with_guardian', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Contact Number')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_institute', to='authority.institute')),
                ('student_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
                ('study_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_class', to='authority.studyclass')),
            ],
            options={
                'verbose_name': 'Student Profile',
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
    ]