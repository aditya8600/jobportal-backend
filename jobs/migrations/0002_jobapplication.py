# Generated by Django 5.2.3 on 2025-06-13 08:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected'), ('hired', 'Hired')], default='pending', max_length=20)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(limit_choices_to={'role': 'candidate'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost')),
            ],
        ),
    ]
