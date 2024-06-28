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

# Generated by Django 3.2.12 on 2022-05-10 07:28

from django.db import migrations, models


from paasng.utils.i18n.migrate import copy_field


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0011_auto_20220510_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploystep',
            name='display_name_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='步骤名称(展示用)'),
        ),
        migrations.AddField(
            model_name='deploystep',
            name='display_name_zh_cn',
            field=models.CharField(max_length=64, null=True, verbose_name='步骤名称(展示用)'),
        ),
        migrations.AddField(
            model_name='deploystepmeta',
            name='display_name_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='步骤名称(展示用)'),
        ),
        migrations.AddField(
            model_name='deploystepmeta',
            name='display_name_zh_cn',
            field=models.CharField(max_length=64, null=True, verbose_name='步骤名称(展示用)'),
        ),
        migrations.RunPython(code=copy_field('engine', 'deploystepmeta', 'name', 'display_name_zh_cn')),
    ]
