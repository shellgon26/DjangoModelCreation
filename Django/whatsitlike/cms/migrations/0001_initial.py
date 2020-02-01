# Generated by Django 2.2.7 on 2019-12-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=120)),
                ('customer_email', models.CharField(max_length=128)),
                ('customer_logo_URL', models.URLField(blank=True)),
                ('customer_CSS_URL', models.URLField(blank=True)),
            ],
        ),
    ]