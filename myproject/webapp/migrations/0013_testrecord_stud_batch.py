# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20160412_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrecord',
            name='stud_batch',
            field=models.IntegerField(null=True),
        ),
    ]
