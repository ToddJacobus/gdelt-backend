# from django.db import models
# Switching over to GeoDjango
from django.contrib.gis.db import models
import architect

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Sources(models.Model):
    gkg_id = models.CharField(max_length=50, unique=True)
    pub_date = models.DateField()
    pub_id = models.IntegerField()
    source_name = models.CharField(max_length=100)
    doc_uri = models.TextField()
    tone = models.FloatField()
    positive_score = models.FloatField()
    negative_score = models.FloatField()
    polarity = models.FloatField()
    activity_ref_density = models.FloatField()
    pronoun_ref_density = models.FloatField()
    word_count = models.FloatField()
    share_image = models.TextField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Counts(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    count_type = models.CharField(max_length=50)
    count_n = models.IntegerField()
    object_type = models.TextField()
    location_type = models.IntegerField()
    location_name = models.TextField()
    location_country = models.CharField(max_length=50)
    location_adm1 = models.CharField(max_length=50)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    location_feature_id = models.CharField(max_length=50)
    geom = models.PointField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Themes(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    theme = models.CharField(max_length=50)
    text_offset = models.IntegerField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Locations(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    location_type = models.IntegerField()
    location_name = models.TextField()
    location_country = models.CharField(max_length=50)
    location_adm1 = models.CharField(max_length=50)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    location_feature_id = models.CharField(max_length=50)
    geom = models.PointField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class People(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    person_name = models.CharField(max_length=100)
    text_offset = models.IntegerField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Orgs(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    org_name = models.CharField(max_length=100)
    text_offset = models.IntegerField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Liwc(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    dimension = models.CharField(max_length=50)
    word_count = models.IntegerField()

@architect.install('partition', type='range', subtype='date', constraint='month', column='pub_date')
class Images(models.Model):
    source_id = models.IntegerField()
    pub_date = models.DateField()
    image_url = models.TextField()





