# Generated by Django 3.1.3 on 2022-04-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220428_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='title',
        ),
    ]
