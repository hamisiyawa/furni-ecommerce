# Generated by Django 4.2.6 on 2023-11-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_app', '0004_pages_has_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
