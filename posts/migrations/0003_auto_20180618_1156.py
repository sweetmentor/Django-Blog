# Generated by Django 2.0.6 on 2018-06-18 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='author',
        ),
    ]
