# Generated by Django 5.1.3 on 2025-01-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0002_alter_studyclass_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institute',
            options={'ordering': ('-id',), 'verbose_name': 'Institute'},
        ),
        migrations.AlterModelOptions(
            name='studyclass',
            options={'ordering': ('-id',), 'verbose_name': 'Study Class'},
        ),
    ]
