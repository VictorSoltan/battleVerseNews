# Generated by Django 3.2.9 on 2021-12-20 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created',
        ),
    ]
