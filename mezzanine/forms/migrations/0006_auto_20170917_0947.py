# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-17 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20151026_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='choices_en',
            field=models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, null=True, verbose_name='Choices'),
        ),
        migrations.AddField(
            model_name='field',
            name='choices_he',
            field=models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, null=True, verbose_name='Choices'),
        ),
        migrations.AddField(
            model_name='field',
            name='default_en',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default value'),
        ),
        migrations.AddField(
            model_name='field',
            name='default_he',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default value'),
        ),
        migrations.AddField(
            model_name='field',
            name='help_text_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Help text'),
        ),
        migrations.AddField(
            model_name='field',
            name='help_text_he',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Help text'),
        ),
        migrations.AddField(
            model_name='field',
            name='label_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Label'),
        ),
        migrations.AddField(
            model_name='field',
            name='label_he',
            field=models.CharField(max_length=200, null=True, verbose_name='Label'),
        ),
        migrations.AddField(
            model_name='field',
            name='placeholder_text_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Placeholder Text'),
        ),
        migrations.AddField(
            model_name='field',
            name='placeholder_text_he',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Placeholder Text'),
        ),
        migrations.AddField(
            model_name='form',
            name='button_text_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Button text'),
        ),
        migrations.AddField(
            model_name='form',
            name='button_text_he',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Button text'),
        ),
        migrations.AddField(
            model_name='form',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='form',
            name='content_he',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='form',
            name='email_message_en',
            field=models.TextField(blank=True, help_text='Emails sent based on the above options will contain each of the form fields entered. You can also enter a message here that will be included in the email.', null=True, verbose_name='Message'),
        ),
        migrations.AddField(
            model_name='form',
            name='email_message_he',
            field=models.TextField(blank=True, help_text='Emails sent based on the above options will contain each of the form fields entered. You can also enter a message here that will be included in the email.', null=True, verbose_name='Message'),
        ),
        migrations.AddField(
            model_name='form',
            name='email_subject_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='form',
            name='email_subject_he',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='form',
            name='response_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Response'),
        ),
        migrations.AddField(
            model_name='form',
            name='response_he',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Response'),
        ),
    ]
