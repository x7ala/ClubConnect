# Generated by Django 5.0 on 2024-05-01 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_eventactivity_edit_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='rejections',
            name='edit_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rejection_reason', to='pages.editeventactivity'),
        ),
    ]
