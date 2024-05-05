# Generated by Django 5.0 on 2024-04-25 19:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_eventactivity_clubname_alter_eventactivity_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventactivity',
            name='clubname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='pages.createclub'),
        ),
        migrations.AlterField(
            model_name='eventactivity',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='clubname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='pages.createclub'),
        ),
    ]