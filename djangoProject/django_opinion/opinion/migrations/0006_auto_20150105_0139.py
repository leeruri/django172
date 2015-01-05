# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0005_auto_20150104_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=250)),
                ('reg_date', models.DateTimeField(default=None)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='opinion',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='opinionuser',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='opinion',
            name='opinion_tags',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opinionuser',
            name='user_email',
            field=models.EmailField(help_text=b'your email adress', unique=True, max_length=75),
            preserve_default=True,
        ),
    ]
