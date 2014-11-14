# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relevance', '0002_remove_jsonstore_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonstore',
            name='books_data',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
