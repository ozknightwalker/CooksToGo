# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipecomponent',
            old_name='ingredients',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='recipecomponent',
            old_name='unitOfMeasure',
            new_name='unit_of_measure',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
    ]
