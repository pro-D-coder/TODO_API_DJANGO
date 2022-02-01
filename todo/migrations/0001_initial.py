# Generated by Django 4.0.1 on 2022-02-01 17:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2022, 2, 1, 17, 26, 31, 814371, tzinfo=utc))),
                ('updateAt', models.DateTimeField(default=datetime.datetime(2022, 2, 1, 17, 26, 31, 814371, tzinfo=utc))),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('INCOMPLETE', 'INCOMPLETE')], default='INCOMPLETE', max_length=10)),
            ],
            options={
                'db_table': 'todo',
            },
        ),
    ]
