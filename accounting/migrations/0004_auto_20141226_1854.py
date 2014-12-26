# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20141226_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='partner_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='partner',
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
