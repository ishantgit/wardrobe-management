# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wardrobe',
            fields=[
                ('user', models.ForeignKey(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
