# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_opinion_id',
            new_name='opinion_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_writer_id',
            new_name='writer_id',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='opinion_link_id',
            new_name='opinion_id',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='opinion_writer_id',
            new_name='writer_id',
        ),
    ]
