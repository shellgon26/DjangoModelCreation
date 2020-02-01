# Generated by Django 3.0 on 2019-12-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20191214_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_primary_colour',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_secondary_colour',
        ),
        migrations.AddField(
            model_name='customer',
            name='css_button_colour',
            field=models.CharField(default='#F49D14', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_button_hover_colour',
            field=models.CharField(default='#F26D0E', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_default_border_colour',
            field=models.CharField(default='#214192', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_focus_border_colour',
            field=models.CharField(default='#F6C532', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_icon_colour',
            field=models.CharField(default='#3580D7', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_icon_hover_colour',
            field=models.CharField(default='#4F9EE9', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_subheading_colour',
            field=models.CharField(default='#2A5EB2', max_length=7),
        ),
        migrations.AddField(
            model_name='customer',
            name='css_title_colour',
            field=models.CharField(default='#214192', max_length=7),
        ),
    ]