# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0008_auto_20150105_0253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinion',
            old_name='opinion_id',
            new_name='linked_opinion_id',
        ),
    ]
