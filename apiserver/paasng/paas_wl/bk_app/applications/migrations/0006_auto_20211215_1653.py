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

# Generated by Django 2.2.17 on 2021-12-15 08:53

import paas_wl.utils.models
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211214_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='procfile',
            field=jsonfield.fields.JSONField(
                blank=True, default={}, validators=[paas_wl.utils.models.validate_procfile]
            ),
        ),
        migrations.AlterField(
            model_name='build',
            name='branch',
            field=models.CharField(help_text='readable version, such as trunk/master', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='revision',
            field=models.CharField(help_text='unique version, such as sha256', max_length=128, null=True),
        ),
    ]
