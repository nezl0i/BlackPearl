# Generated by Django 4.1.2 on 2022-10-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='id_post_comments',
            new_name='post_comments',
        ),
    ]
