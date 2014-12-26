# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20141226_1854'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PartnerType',
        ),
    ]
