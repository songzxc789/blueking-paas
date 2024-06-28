# -*- coding: utf-8 -*-
# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.

# Generated by Django 2.2.17 on 2020-11-27 02:50

import blue_krill.models.fields
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import paasng.utils.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, verbose_name='方案名称')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='方案简介')),
                ('config', blue_krill.models.fields.EncryptField(default='', verbose_name='方案配置')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('region', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=64, verbose_name='服务名称')),
                ('display_name', models.CharField(max_length=128, verbose_name='服务全称')),
                ('logo', paasng.utils.models.ImageField(null=True, upload_to='service-logo', verbose_name='服务logo')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='服务简介')),
                ('long_description', models.TextField(blank=True, verbose_name='服务详细介绍')),
                ('instance_tutorial', models.TextField(blank=True, verbose_name='服务markdown介绍')),
                ('available_languages', models.CharField(blank=True, max_length=1024, null=True, verbose_name='支持编程语言')),
                ('config', jsonfield.fields.JSONField(default={})),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('is_visible', models.BooleanField(default=True, verbose_name='是否可见')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='分类名称')),
                ('sort_priority', models.IntegerField(default=0, verbose_name='排序权重')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceInstance',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('config', jsonfield.fields.JSONField(default={})),
                ('credentials', blue_krill.models.fields.EncryptField(default='')),
                ('to_be_deleted', models.BooleanField(default=False)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Plan')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ServiceCategory', verbose_name='服务分类'),
        ),
        migrations.CreateModel(
            name='ResourceId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(max_length=32)),
                ('uid', models.CharField(db_index=True, max_length=64, unique=True)),
            ],
            options={
                'unique_together': {('namespace', 'uid')},
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('region', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together={('service', 'name')},
        ),
    ]
