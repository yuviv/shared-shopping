# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IOU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'u', max_length=1, choices=[(b'u', b'Unpaid'), (b'p', b'Paid'), (b'c', b'Confirmed')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('status', models.CharField(default=b'n', max_length=1, choices=[(b'n', b'Need'), (b'b', b'Bought')])),
                ('num_people_split', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('num_of_people', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('shopping_list', models.ForeignKey(to='manager.ShoppingList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='bought_by',
            field=models.ForeignKey(to='manager.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='shopping_list',
            field=models.ForeignKey(to='manager.ShoppingList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iou',
            name='item',
            field=models.ForeignKey(to='manager.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iou',
            name='payer',
            field=models.ForeignKey(related_name=b'payer', to='manager.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iou',
            name='receiver',
            field=models.ForeignKey(related_name=b'receiver', to='manager.User'),
            preserve_default=True,
        ),
    ]
