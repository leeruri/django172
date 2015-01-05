# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0009_auto_20150105_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, unpack_ipv4=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinion',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, unpack_ipv4=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinionuser',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, unpack_ipv4=True, blank=True),
            preserve_default=True,
        ),
    ]
