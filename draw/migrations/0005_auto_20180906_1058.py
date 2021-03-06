# Generated by Django 2.1 on 2018-09-06 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0004_tickets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sjanse',
            old_name='trekknings_dato',
            new_name='kjopt_dato',
        ),
        migrations.AddField(
            model_name='tickets',
            name='lot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='draw.Sjanse'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets',
            name='trekknings_dato',
            field=models.DateField(default=datetime.datetime(2018, 9, 6, 10, 58, 34, 153521, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickets',
            name='all_tickets',
            field=models.IntegerField(),
        ),
    ]
