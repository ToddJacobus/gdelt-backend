from django.db import models
import architect

# Create your models here.
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


class Counts(modesl.Model):
    source_id = models.Integer
    # TODO: finish me....