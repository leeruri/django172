# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0010_auto_20150105_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-reg_date']},
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='opinion_tags',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.AddField(
            model_name='opinion',
            name='tag_name',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=250, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
