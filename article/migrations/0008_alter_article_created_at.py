# Generated by Django 3.2.9 on 2021-12-20 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 12, 20, 17, 30, 57, 527446, tzinfo=utc)),
        ),
    ]
