# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_wagtailsitepage_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuelement',
            name='css_class',
            field=models.CharField(blank=True, null=True, help_text='Optional styling for the menu item', verbose_name='CSS Class', max_length=255),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='explicit_name',
            field=models.CharField(blank=True, null=True, help_text='If you want a different name than the page title.', max_length=64),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='icon_class',
            field=models.CharField(blank=True, null=True, help_text='In case you need an icon element <i> for the menu item', verbose_name='Icon Class', max_length=255),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='link_document',
            field=models.ForeignKey(null=True, help_text='Choose an existing document if you want the link to open a document.', on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.Document', blank=True, related_name='+'),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='link_email',
            field=models.EmailField(blank=True, null=True, help_text='Set the recipient email address if you want the link to send an email.', max_length=254),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='link_external',
            field=models.URLField(blank=True, null=True, help_text='Set an external link if you want the link to point somewhere outside the CMS.', verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='link_page',
            field=models.ForeignKey(null=True, help_text='Choose an existing page if you want the link to point somewhere inside the CMS.', on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page', blank=True, related_name='+'),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='link_phone',
            field=models.CharField(blank=True, null=True, help_text='Set the number if you want the link to dial a phone number.', max_length=20),
        ),
        migrations.AlterField(
            model_name='menuelement',
            name='short_name',
            field=models.CharField(blank=True, null=True, help_text='If you need a custom name for responsive devices.', max_length=32),
        ),
        migrations.AlterField(
            model_name='submitformfield',
            name='choices',
            field=models.CharField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='Choices', max_length=512),
        ),
        migrations.AlterField(
            model_name='submitformfield',
            name='default_value',
            field=models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', verbose_name='Default value', max_length=255),
        ),
        migrations.AlterField(
            model_name='submitformfield',
            name='field_type',
            field=models.CharField(max_length=16, choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], verbose_name='Field type'),
        ),
        migrations.AlterField(
            model_name='submitformfield',
            name='help_text',
            field=models.CharField(blank=True, verbose_name='Help text', max_length=255),
        ),
        migrations.AlterField(
            model_name='submitformfield',
            name='label',
            field=models.CharField(max_length=255, help_text='The label of the form field', verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='submitformfield',
            name='required',
            field=models.BooleanField(default=True, verbose_name='Required'),
        ),
        migrations.AlterField(
            model_name='submitformpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Edit the content you want to see before the form.'),
        ),
        migrations.AlterField(
            model_name='submitformpage',
            name='from_address',
            field=models.CharField(blank=True, verbose_name='From address', max_length=255),
        ),
        migrations.AlterField(
            model_name='submitformpage',
            name='subject',
            field=models.CharField(blank=True, verbose_name='Subject', max_length=255),
        ),
        migrations.AlterField(
            model_name='submitformpage',
            name='thank_you_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Set the message users will see after submitting the form.'),
        ),
        migrations.AlterField(
            model_name='submitformpage',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to this address', verbose_name='To address', max_length=255),
        ),
        migrations.AlterField(
            model_name='wagtailcompanypage',
            name='company_url',
            field=models.URLField(blank=True, null=True, help_text='Paste the URL of your site, something like "http://www.springload.co.nz"'),
        ),
        migrations.AlterField(
            model_name='wagtailsitepage',
            name='is_featured',
            field=models.BooleanField(help_text='If enabled, this site will appear on top of the sites list of the homepage.', default=False, verbose_name='Featured'),
        ),
        migrations.AlterField(
            model_name='wagtailsitepage',
            name='site_url',
            field=models.URLField(null=True, help_text='Paste the URL of your site, something like "http://www.springload.co.nz"'),
        ),
    ]
