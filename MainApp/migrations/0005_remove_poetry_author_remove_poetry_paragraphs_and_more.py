# Generated by Django 4.0.1 on 2022-03-08 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_rule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poetry',
            name='author',
        ),
        migrations.RemoveField(
            model_name='poetry',
            name='paragraphs',
        ),
        migrations.RemoveField(
            model_name='poetry',
            name='rhythmic',
        ),
    ]
