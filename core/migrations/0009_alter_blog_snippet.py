# Generated by Django 4.0.6 on 2022-07-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_blog_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='snippet',
            field=models.TextField(blank=True),
        ),
    ]
