# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_on', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(to='item.Item')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='itemhistory',
            unique_together=set([('item', 'date_on')]),
        ),
    ]
