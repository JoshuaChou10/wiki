# Generated by Django 4.2.6 on 2023-10-13 02:13

import apps.wiki.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Last Modified')),
                ('date_created', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Creation Date')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=32767, verbose_name='Description')),
                ('slug', models.CharField(max_length=255, null=True, validators=[apps.wiki.models.validate_slug], verbose_name='Slug')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_categories', to='wiki.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Last Modified')),
                ('date_created', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Creation Date')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.CharField(blank=True, default='', max_length=32767, verbose_name='Description')),
                ('slug', models.CharField(max_length=255, validators=[apps.wiki.models.validate_slug], verbose_name='Slug')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='child_pages', to='wiki.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'db_table': 'Page',
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Last Modified')),
                ('date_created', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Creation Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order #')),
                ('content', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.textcontent', verbose_name='Text Content')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='revisions', to='wiki.page', verbose_name='Page')),
                ('rollback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rollbacks', to='wiki.revision')),
            ],
            options={
                'verbose_name': 'Revision',
                'verbose_name_plural': 'Revisions',
                'db_table': 'Revision',
            },
        ),
        migrations.AddConstraint(
            model_name='revision',
            constraint=models.CheckConstraint(check=models.Q(('rollback__isnull', False), ('content__isnull', False), _connector='OR'), name='not_both_null'),
        ),
    ]
