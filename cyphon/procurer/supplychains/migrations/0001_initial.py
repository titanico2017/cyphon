# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requisitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldCoupling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=64, verbose_name='field name')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_couplings', related_query_name='field_coupling', to='requisitions.Parameter', verbose_name='parameter')),
            ],
            options={
                'ordering': ['supply_link', 'parameter'],
                'verbose_name': 'supply link',
                'verbose_name_plural': 'supply links',
            },
        ),
        migrations.CreateModel(
            name='SupplyChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'supply chain',
                'verbose_name_plural': 'supply chains',
            },
        ),
        migrations.CreateModel(
            name='SupplyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('position', models.IntegerField(default=0, help_text='An integer representing the order of this step in the Supply Chain. Steps are performed in ascending order, with the lowest number performed first.', verbose_name='position')),
                ('requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitions.Requisition', verbose_name='requisition')),
                ('supply_chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplylinks', related_query_name='supplylink', to='supplychains.SupplyChain', verbose_name='supply chain')),
            ],
            options={
                'ordering': ['supply_chain', 'position'],
                'verbose_name': 'supply link',
                'verbose_name_plural': 'supply links',
            },
        ),
        migrations.AddField(
            model_name='fieldcoupling',
            name='supply_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_couplings', related_query_name='field_coupling', to='supplychains.SupplyLink', verbose_name='supply link'),
        ),
        migrations.AlterUniqueTogether(
            name='supplylink',
            unique_together=set([('supply_chain', 'position')]),
        ),
        migrations.AlterUniqueTogether(
            name='fieldcoupling',
            unique_together=set([('supply_link', 'parameter')]),
        ),
    ]
