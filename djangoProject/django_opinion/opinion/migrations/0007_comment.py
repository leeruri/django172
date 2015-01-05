# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0006_auto_20150105_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_contents', models.TextField()),
                ('comment_writer_id', models.CharField(max_length=10, blank=True)),
                ('comment_opinion_id', models.CharField(max_length=10, blank=True)),
                ('ip_address', models.GenericIPAddressField(unpack_ipv4=True)),
                ('reg_date', models.DateTimeField(default=None)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
    ]
