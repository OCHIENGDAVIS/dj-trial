# Generated by Django 4.2.2 on 2023-06-24 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created', '-updated']},
        ),
    ]
