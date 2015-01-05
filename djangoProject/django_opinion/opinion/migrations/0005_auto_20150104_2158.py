# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0004_auto_20150104_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinionuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opinionuser',
            name='user_email',
            field=models.EmailField(help_text=b'your email adress', unique=True, max_length=75, verbose_name=b"users's email "),
            preserve_default=True,
        ),
    ]
