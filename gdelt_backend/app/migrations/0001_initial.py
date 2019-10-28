# Generated by Django 2.2.6 on 2019-10-28 12:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('count_type', models.CharField(max_length=50)),
                ('count_n', models.IntegerField()),
                ('object_type', models.TextField()),
                ('location_type', models.IntegerField()),
                ('location_name', models.TextField()),
                ('location_country', models.CharField(max_length=50)),
                ('location_adm1', models.CharField(max_length=50)),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('location_feature_id', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('image_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Liwc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('dimension', models.CharField(max_length=50)),
                ('word_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('location_type', models.IntegerField()),
                ('location_name', models.TextField()),
                ('location_country', models.CharField(max_length=50)),
                ('location_adm1', models.CharField(max_length=50)),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('location_feature_id', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Orgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('org_name', models.CharField(max_length=100)),
                ('text_offset', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('person_name', models.CharField(max_length=100)),
                ('text_offset', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gkg_id', models.CharField(max_length=50, unique=True)),
                ('pub_date', models.DateField()),
                ('pub_id', models.IntegerField()),
                ('source_name', models.CharField(max_length=100)),
                ('doc_uri', models.TextField()),
                ('tone', models.FloatField()),
                ('positive_score', models.FloatField()),
                ('negative_score', models.FloatField()),
                ('polarity', models.FloatField()),
                ('activity_ref_density', models.FloatField()),
                ('pronoun_ref_density', models.FloatField()),
                ('word_count', models.FloatField()),
                ('share_image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('theme', models.CharField(max_length=50)),
                ('text_offset', models.IntegerField()),
            ],
        ),
    ]