# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordem', '0002_remove_ordem_codigo_consulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='codigo_consulta',
            field=models.CharField(default='0000000000', max_length=10, editable=False),
        ),
    ]
