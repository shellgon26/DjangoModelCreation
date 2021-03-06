# Generated by Django 3.0 on 2019-12-16 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_bundle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBundleLink',
            fields=[
                ('link_id', models.AutoField(primary_key=True, serialize=False)),
                ('bundle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Bundle')),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Content')),
            ],
        ),
    ]
