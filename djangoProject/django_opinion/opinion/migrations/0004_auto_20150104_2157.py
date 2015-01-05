# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0003_auto_20150104_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinionuser',
            name='user_area',
            field=models.CharField(blank=True, max_length=1, choices=[(b'K', b'\xea\xb5\xad\xeb\x82\xb4'), (b'O', b'\xed\x95\xb4\xec\x99\xb8'), (b'N', b'\xea\xb8\xb0\xed\x83\x80')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinion',
            name='opinion_link_id',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinion',
            name='opinion_writer_id',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinionuser',
            name='user_email',
            field=models.EmailField(primary_key=True, serialize=False, max_length=75, help_text=b'your email adress', unique=True, verbose_name=b"users's email "),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinionuser',
            name='user_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
