# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opnion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opnion_title', models.CharField(max_length=250)),
                ('opnion_contents', models.TextField()),
                ('opnion_writer_id', models.CharField(max_length=10)),
                ('opnion_link_id', models.CharField(max_length=10)),
                ('ip_address', models.GenericIPAddressField(unpack_ipv4=True)),
                ('reg_date', models.DateTimeField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpnionUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(max_length=75)),
                ('user_nickname', models.CharField(max_length=50)),
                ('user_pwd', models.CharField(max_length=50)),
                ('user_url', models.URLField(blank=True)),
                ('ip_address', models.GenericIPAddressField(unpack_ipv4=True)),
                ('reg_date', models.DateTimeField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
