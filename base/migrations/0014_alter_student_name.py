# Generated by Django 4.2.2 on 2023-06-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_author_blog_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]