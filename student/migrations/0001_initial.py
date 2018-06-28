# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-28 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('s_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='学号')),
                ('s_contact', models.CharField(default='无', max_length=20, verbose_name='联系方式')),
                ('s_isconfirm', models.BooleanField(default=False, verbose_name='导师确认')),
                ('s_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.Department', verbose_name='院系')),
                ('s_major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.Major', verbose_name='专业')),
            ],
            options={
                'verbose_name': '学生资料',
                'verbose_name_plural': '学生资料',
                'ordering': ['s_id'],
                'permissions': (('is_student', 'is a student'),),
            },
        ),
    ]
