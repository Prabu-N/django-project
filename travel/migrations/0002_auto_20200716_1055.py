# Generated by Django 3.0.7 on 2020-07-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prabu',
            name='sp1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='prabu',
            name='sp2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='prabu',
            name='sp3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='prabu',
            name='sp4',
            field=models.TextField(blank=True),
        ),
    ]
