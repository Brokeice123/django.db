# Generated by Django 4.1.7 on 2023-03-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoregistrationKeith', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True, default=254, max_length=50),
            preserve_default=False,
        ),
    ]