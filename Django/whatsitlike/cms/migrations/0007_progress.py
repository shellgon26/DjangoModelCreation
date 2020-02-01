# Generated by Django 3.0 on 2019-12-16 20:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_contentviewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('progress_id', models.AutoField(primary_key=True, serialize=False)),
                ('progress_value', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Content')),
                ('viewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.ContentViewer')),
            ],
        ),
    ]
