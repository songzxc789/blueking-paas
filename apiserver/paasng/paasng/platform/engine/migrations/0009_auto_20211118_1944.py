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

# Generated by Django 2.2.17 on 2021-11-18 11:44

from django.db import migrations, models
import jsonfield.fields
import paasng.platform.modules.models.deploy_config


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0008_auto_20211116_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='hooks',
            field=paasng.platform.modules.models.deploy_config.HookListField(default=list, help_text='部署钩子'),
        ),
        migrations.AddField(
            model_name='deployment',
            name='procfile',
            field=jsonfield.fields.JSONField(default=dict, help_text='部署命令'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='pre_release_status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                default='pending', max_length=16),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='release_status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                default='pending', max_length=16),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                default='pending', max_length=16, verbose_name='部署状态'),
        ),
        migrations.AlterField(
            model_name='deployphase',
            name='status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                max_length=32, null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='deploystep',
            name='status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                max_length=32, null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='moduleenvironmentoperations',
            name='status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                default='pending', max_length=16, verbose_name='操作状态'),
        ),
        migrations.AlterField(
            model_name='offlineoperation',
            name='status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                default='pending', max_length=16, verbose_name='下线状态'),
        ),
        migrations.AlterField(
            model_name='oneoffcommand',
            name='status',
            field=models.CharField(
                choices=[('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')],
                default='pending', max_length=16),
        ),
    ]
