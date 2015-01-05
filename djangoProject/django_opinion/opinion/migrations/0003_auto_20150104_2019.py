# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0002_auto_20150104_1926'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Opnion',
            new_name='Opinion',
        ),
        migrations.RenameModel(
            old_name='OpnionUser',
            new_name='OpinionUser',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='opnion_contents',
            new_name='opinion_contents',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='opnion_link_id',
            new_name='opinion_link_id',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='opnion_title',
            new_name='opinion_title',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='opnion_writer_id',
            new_name='opinion_writer_id',
        ),
    ]
