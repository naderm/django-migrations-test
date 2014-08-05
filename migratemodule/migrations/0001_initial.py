# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.CharField(default=b'Sp', max_length=2, choices=[(b'Sp', b'Spring'), (b'Su', b'Summer'), (b'Fa', b'Fall')])),
                ('year', models.PositiveSmallIntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='modeltest',
            unique_together=set([(b'season', b'year')]),
        ),
    ]
