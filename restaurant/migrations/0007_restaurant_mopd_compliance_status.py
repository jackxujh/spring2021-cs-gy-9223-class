# Generated by Django 3.1.7 on 2021-03-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_accessibilityrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='mopd_compliance_status',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
