# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20141215_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
    ]
