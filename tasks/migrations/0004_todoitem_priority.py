# Generated by Django 3.1.6 on 2021-02-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_todoitem_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.IntegerField(choices=[(1, 'High priority'), (2, 'Medium priority'), (3, 'Low priority')], default=2, verbose_name='Priority'),
        ),
    ]
