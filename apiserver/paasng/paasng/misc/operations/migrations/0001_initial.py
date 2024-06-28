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

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import paasng.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(help_text='部署区域', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', paasng.utils.models.BkUserField(blank=True, db_index=True, max_length=64, null=True)),
                ('type', models.SmallIntegerField(db_index=True, help_text='操作类型')),
                ('is_hidden', models.BooleanField(default=False, help_text='隐藏起来')),
                ('source_object_id', models.CharField(blank=True, default='', help_text='事件来源对象ID，具体指向需要根据操作类型解析', max_length=32, null=True)),
                ('module_name', models.CharField(max_length=20, null=True, verbose_name='关联 Module')),
                ('extra_values', jsonfield.fields.JSONField(blank=True, default={}, help_text='操作额外信息')),
                ('application', models.ForeignKey(blank=True, help_text='操作的PAAS应用', null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.Application')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationLatestOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.SmallIntegerField(help_text='操作类型')),
                ('latest_operated_at', models.DateTimeField(db_index=True)),
                ('application', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='latest_op', to='applications.Application')),
                ('operation', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='operations.Operation')),
            ],
        ),
    ]
