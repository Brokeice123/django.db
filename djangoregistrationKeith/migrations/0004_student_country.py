# Generated by Django 4.1.7 on 2023-03-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoregistrationKeith', '0003_student_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]